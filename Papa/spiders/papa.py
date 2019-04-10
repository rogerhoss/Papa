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
import pkgutil

class Papa(BasePortiaSpider):
    name = "papa"
    allowed_domains = ['www.pbcgov.org']
    file = pkgutil.get_data("Papa", "resources/winners.txt")
    normalContent = file.decode('ascii')
    lines = normalContent.splitlines()
    index = 0
    start_urls = []
    while (index < len(lines)):
        start_urls.append ('https://www.pbcgov.org/papa/Asps/PropertyDetail/PropertyDetail.aspx?parcel='+lines[index])
        index += 1

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
