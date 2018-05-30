import scrapy

class AmazonItem(scrapy.Item):
  product_name = scrapy.Field()
  product_sale_price = scrapy.Field()
