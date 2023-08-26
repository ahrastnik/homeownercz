from urllib.parse import urljoin

import scrapy
from scrapy_playwright.page import PageMethod

from crawler.items import PropertyItem


class PropertySpider(scrapy.Spider):
    name = 'property'

    def __init__(
        self,
        name=None,
        scrape_limit=500,
        domain="https://www.sreality.cz",
        rel_url="/en/search/for-sale/apartments/",
        **kwargs
    ):
        super().__init__(name, **kwargs)
        self.scrape_limit = int(scrape_limit)
        self.REQUEST_META = dict(
            playwright=True,
            playwright_include_page=True,
            playwright_page_methods=[
                PageMethod('wait_for_selector', 'div.dir-property-list'),
            ],
            errback=self.error_callback,
        )
        self.domain = domain
        self.url = urljoin(domain, rel_url)

    def start_requests(self):
        yield scrapy.Request(self.url, meta=self.REQUEST_META)

    def has_reached_scrape_limit(self):
        scrape_count = self.crawler.stats.get_value(
            'properties/scraped_count', default=0
        )
        return scrape_count >= self.scrape_limit

    def parse(self, response):
        for prop in response.css('div.property'):
            if self.has_reached_scrape_limit():
                return

            property_item = PropertyItem(
                {
                    'name': prop.css('span.name::text').get(),
                    'locality': prop.css('span.locality::text').get(),
                    'price': prop.css('span.norm-price::text').get(),
                    'url': urljoin(self.domain, prop.css('a.title::attr(href)').get()),
                    'image_url': prop.css(
                        'a._2vc3VMce92XEJFrv8_jaeN img::attr(src)'
                    ).get(),
                }
            )
            self.crawler.stats.inc_value('properties/scraped_count')
            yield property_item

        next_page = response.css('li.paging-item a.paging-next::attr(href)').get()
        if not next_page or self.has_reached_scrape_limit():
            return
        next_url = urljoin(self.domain, next_page)  # Make an absolute URL

        yield response.follow(next_url, callback=self.parse, meta=self.REQUEST_META)

    async def error_callback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
