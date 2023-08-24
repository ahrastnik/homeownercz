import scrapy
from scrapy_playwright.page import PageMethod

from crawler.items import PropertyItem


class PropertySpider(scrapy.Spider):
    name = 'property'

    def start_requests(self):
        url = "https://www.sreality.cz/en/search/for-sale/apartments/"
        yield scrapy.Request(url, meta=dict(
            playwright=True,
            playwright_include_page=True,
            playwright_page_methods=[
                PageMethod('wait_for_selector', 'div.property'),
            ],
            errback=self.error_callback,
        ))

    def parse(self, response):
        for prop in response.css('div.property'):
            property_item = PropertyItem()
            property_item['name'] = prop.css('span.name::text').get()
            property_item['locality'] = prop.css('span.locality::text').get()
            property_item['price'] = prop.css('span.norm-price::text').get()
            yield property_item
    
    async def error_callback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
