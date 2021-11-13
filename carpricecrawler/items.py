# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarpricecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    product_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    mileage = scrapy.Field()
    lastPlateNumber = scrapy.Field()
    color = scrapy.Field()
    gear = scrapy.Field()
    cartype = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()
    accessories = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zipCode = scrapy.Field()
    post_date = scrapy.Field()
    post_time = scrapy.Field()
    thumb_url = scrapy.Field()
    is_featured = scrapy.Field()
    list_position = scrapy.Field()
