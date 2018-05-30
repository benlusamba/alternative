# -*- coding: utf-8 -*-

BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'


ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'amazon.pipelines.AmazonPipeline': 300,
}


#Define output format and name:
FEED_FORMAT = "csv"
FEED_URI = "amazon.csv"
