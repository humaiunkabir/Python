# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HospitaldatascraperItem(scrapy.Item):
    # define the fields for your item here like:
    doctorName = scrapy.Field()
    speciality = scrapy.Field()
    degree = scrapy.Field()
    doctorDetailsLink = scrapy.Field()
    department = scrapy.Field()
    ## doctorDetails = scrapy.Field()