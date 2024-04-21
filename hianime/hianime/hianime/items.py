# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HianimeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class AnimeItem(scrapy.Item):
    image = scrapy.Field()
    title = scrapy.Field()
    overview = scrapy.Field()
    japanese =  scrapy.Field()
    aired =  scrapy.Field()
    premiered = scrapy.Field()
    duration = scrapy.Field()
    status = scrapy.Field()
    mal_score = scrapy.Field()
    studios = scrapy.Field()
    producers = scrapy.Field()