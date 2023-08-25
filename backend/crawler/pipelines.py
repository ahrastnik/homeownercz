# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

from homeownercz.models import Property


class PropertyPipeline:
    async def process_item(self, item, spider):
        # Property key is used as a key identifier, that's why it is required
        property_url = item.get('url')
        if not property_url:
            raise DropItem(f'Missing URL in {item}')
        # Create a property object from scraped data or update it in the database
        await Property.objects.aupdate_or_create(url=property_url, defaults=item)
        return item
