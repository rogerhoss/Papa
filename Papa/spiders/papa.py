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
    start_urls = [
        'https://www.pbcgov.org/papa/Asps/PropertyDetail/PropertyDetail.aspx?parcel=06434716080080090']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=('.*')
            ),
            callback='parse_item',
            follow=True
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
                        'Location_Address',
                        'div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tr:nth-child(2) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tr:nth-child(2) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > .TDValueLeft > span *::text',
                        []),
                    Field(
                        'Municipality',
                        'div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tr:nth-child(3) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tr:nth-child(3) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > .TDValueLeft > span *::text',
                        []),
                    Field(
                        'Parcel_Control_Number',
                        'div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tr:nth-child(4) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tr:nth-child(4) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tbody > tr:nth-child(4) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(4) > .TDValueLeft > span *::text',
                        []),
                    Field(
                        'Subdivision',
                        'div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tr:nth-child(5) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tr:nth-child(5) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > .TDValueLeft > span *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > .TDValueLeft > span *::text',
                        []),
                    Field(
                        'Official_Record',
                        'div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tr:nth-child(6) > .TDValueLeft *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tr:nth-child(6) > .TDValueLeft *::text, div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tbody > tr:nth-child(6) > .TDValueLeft *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(6) > .TDValueLeft *::text',
                        []),
                    Field(
                        'Sale_Date',
                        'div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tr:nth-child(7) > .TDValueLeft *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tr:nth-child(7) > .TDValueLeft *::text, div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tbody > tr:nth-child(7) > .TDValueLeft *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(7) > .TDValueLeft *::text',
                        []),
                    Field(
                        'Legal_Description',
                        'div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tr:nth-child(8) > .auto-style2 > span *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tr:nth-child(8) > .auto-style2 > span *::text, div:nth-child(3) > fieldset > div > table > tr > td:nth-child(1) > table > tbody > tr:nth-child(8) > .auto-style2 > span *::text, div:nth-child(3) > fieldset > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(8) > .auto-style2 > span *::text',
                        []),
                    Field(
                        'Owners',
                        'div:nth-child(4) > fieldset > table > tr:nth-child(2) > td:nth-child(1) > table *::text, div:nth-child(4) > fieldset > table > tbody > tr:nth-child(2) > td:nth-child(1) > table *::text',
                        []),
                    Field(
                        'Owner_1',
                        'div:nth-child(4) > fieldset > table > tr:nth-child(2) > td:nth-child(1) > table > tr:nth-child(2) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tbody > tr:nth-child(2) > td:nth-child(1) > table > tr:nth-child(2) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tr:nth-child(2) > td:nth-child(1) > table > tbody > tr:nth-child(2) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tbody > tr:nth-child(2) > td:nth-child(1) > table > tbody > tr:nth-child(2) > .TDValueLeft *::text',
                        []),
                    Field(
                        'Owner_2',
                        'div:nth-child(4) > fieldset > table > tr:nth-child(2) > td:nth-child(1) > table > tr:nth-child(3) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tbody > tr:nth-child(2) > td:nth-child(1) > table > tr:nth-child(3) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tr:nth-child(2) > td:nth-child(1) > table > tbody > tr:nth-child(3) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tbody > tr:nth-child(2) > td:nth-child(1) > table > tbody > tr:nth-child(3) > .TDValueLeft *::text',
                        []),
                    Field(
                        'Mailing_Address',
                        'div:nth-child(4) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > table *::text, div:nth-child(4) > fieldset > table > tbody > tr:nth-child(2) > td:nth-child(2) > table *::text',
                        []),
                    Field(
                        'Mailing_Line_1',
                        'div:nth-child(4) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > table > tr:nth-child(2) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tr:nth-child(2) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(2) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(2) > .TDValueLeft *::text',
                        []),
                    Field(
                        'Mailing_Line_2',
                        'div:nth-child(4) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > table > tr:nth-child(4) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tr:nth-child(4) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(4) > .TDValueLeft *::text, div:nth-child(4) > fieldset > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(4) > .TDValueLeft *::text',
                        []),
                    Field(
                        'Sales_Information',
                        'div:nth-child(5) > fieldset *::text',
                        []),
                    Field(
                        'Exemption_Information',
                        'div:nth-child(6) > fieldset *::text',
                        []),
                    Field(
                        'Appraisals',
                        'div:nth-child(8) > fieldset *::text',
                        [])])]]
