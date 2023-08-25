from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = 'Release the spiders'

    def handle(self, *args, **options):
        # Run the Scrapy property crawler once
        process = CrawlerProcess(get_project_settings())
        process.crawl('property')
        process.start()
