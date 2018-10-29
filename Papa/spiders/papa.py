from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem, PropertyAppraiserPalmBeachCountyFloridaUsaItem, PropertyAppraiserPalmBeachCountyFloridaUsa1Item


class Papa(BasePortiaSpider):
    name = "papa"
    allowed_domains = ['www.pbcgov.org']
    start_urls = []
    baseurl = 'https://www.pbcgov.org/papa/Asps/PropertyDetail/PropertyDetail.aspx?parcel=064347160800'
    parcelnum = 1100  #Starting Parcel Number
    while parcelnum <= 1115:  # Ending Parcel Number
        start_urls.append (baseurl + str(parcelnum) + '0')
        parcelnum += 1
    #  print (start_urls)
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=False
        )
    ]
    items = [
        [
            Item(
                PropertyAppraiserPalmBeachCountyFloridaUsa1Item,
                None,
                '#MainContent_divRealProperty',
                [
                    Field(
                        'property_detail',
                        'div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) *::text',
                        []),
                    Field(
                        'owner_information',
                        'div:nth-child(4) > fieldset *::text',
                        []),
                    Field(
                        'sales_information',
                        'div:nth-child(5) > fieldset > table > tr:nth-child(1) > td > div *::text, div:nth-child(5) > fieldset > table > tbody > tr:nth-child(1) > td > div *::text',
                        []),
                    Field(
                        'exemption_information',
                        'div:nth-child(6) > fieldset *::text',
                        []),
                    Field(
                        'property_information',
                        'div:nth-child(7) > fieldset *::text',
                        []),
                    Field(
                        'appraisals',
                        'div:nth-child(8) > fieldset > table > tr:nth-child(1) > td > table *::text, div:nth-child(8) > fieldset > table > tbody > tr:nth-child(1) > td > table *::text',
                        []),
                    Field(
                        'assessed_values',
                        'div:nth-child(9) > fieldset > table > tr > td:nth-child(1) > table *::text, div:nth-child(9) > fieldset > table > tbody > tr > td:nth-child(1) > table *::text',
                        []),
                    Field(
                        'taxes',
                        'div:nth-child(10) > fieldset > table > tr:nth-child(1) > td > table *::text, div:nth-child(10) > fieldset > table > tbody > tr:nth-child(1) > td > table *::text',
                        [])])]]
