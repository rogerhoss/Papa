from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class PropertyAppraiserPalmBeachCountyFloridaUsa1Item(PortiaItem):
    Owner_1 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Legal_Description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Municipality = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Official_Record = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Mailing_Line_1 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Owner_2 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Parcel_Control_Number = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Location_Address = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Subdivision = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Mailing_Line_2 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Sale_Date = scrapy.Field(
        input_processor=Date(),
        output_processor=Join(),
    )


class PropertyAppraiserPalmBeachCountyFloridaUsaItem(PortiaItem):
    Parcel_Control_Number = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Location_Address = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
