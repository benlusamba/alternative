# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem

class AmazoncpiSpider(scrapy.Spider):
    name = 'AmazonCPI'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/Goodthreads-Short-Sleeve-Crewneck-T-Shirt-XX-Large/dp/B078L7HR8J/ref=sr_1_1?s=apparel&ie=UTF8&qid=1527702344&sr=1-1&nodeID=7147441011&psd=1&keywords=tshirt%2Bmen&refinements=p_89%3AGoodthreads&th=1', 'https://www.amazon.com/LOOKFACE-Womens-Shirt-Junior-Graphic/dp/B078SMK43Z/ref=sr_1_9?s=apparel&ie=UTF8&qid=1527703394&sr=8-9&keywords=tshirt+women',
    'https://www.amazon.com/gp/product/B01M5KZQF6/ref=s9_acsd_newrz_hd_bw_bkObD_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=GH21GH1PMYBJC3BWPZVQ&pf_rd_t=101&pf_rd_p=01983785-5025-5625-8e4c-0b4c428e41a5&pf_rd_i=11057651&th=1', 'https://www.amazon.com/gp/product/B001459IEE/ref=s9_acsd_top_hd_bw_bkPOZ_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=GKZ9Q76NWKFF9ASDDGFK&pf_rd_t=101&pf_rd_p=3217ddbe-cff3-53c6-b158-d9e71d60e990&pf_rd_i=11060711',
    'https://www.amazon.com/gp/product/B000WDOZ0Q/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-fresh-search-7&pf_rd_r=KP07WV08WJ9H8NM3NMRJ&pf_rd_r=KP07WV08WJ9H8NM3NMRJ&pf_rd_t=101&pf_rd_p=447245fa-f625-48ea-9313-6a9150394f49&pf_rd_p=447245fa-f625-48ea-9313-6a9150394f49&pf_rd_i=11608002011&ppw=fresh',
    'https://www.amazon.com/HP-Touchscreen-Quad-Core-Keyboard-Speakers/dp/B0795G7Q3H/ref=sr_1_1_sspa?s=electronics&ie=UTF8&qid=1527705388&sr=1-1-spons&keywords=laptop&psc=1']

    def parse(self, response):
        items = AmazonItem()
        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
        items['product_name'] = ''.join(title).strip()
        items['product_sale_price'] = ''.join(sale_price).strip()
        yield items
