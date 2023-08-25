# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyItem(scrapy.Item):
    name = scrapy.Field()
    locality = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()
