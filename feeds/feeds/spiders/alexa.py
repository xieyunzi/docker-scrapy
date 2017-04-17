# -*- coding: utf-8 -*-

import scrapy
from .. import items


class AlexaSpider(scrapy.Spider):
    name = "alexa"
    allowed_domains = ["http://www.alexa.com/topsites"]

    def start_requests(self):
        urls = [
            {'group': 'global', 'url': 'http://www.alexa.com/topsites/'},
            {'group': 'cn', 'url': 'http://www.alexa.com/topsites/countries/CN'},
            {'group': 'us', 'url': 'http://www.alexa.com/topsites/countries/US'},
        ]

        for d in urls:
            yield scrapy.Request(d['url'], meta={'group': d['group']})

    def parse(self, response):

        sites = response.selector.css('.AlexaTable .listings .site-listing')
        for site in sites:
            group = response.meta.get('group')

            item = items.SiteItem()
            item['_type'] = 'site'
            item['_group'] = group
            item['rank'] = site.css('.number::text').extract()[0]
            item['domain'] = site.css('.DescriptionCell > p > a::text').extract()[0]

            desc = site.css('.DescriptionCell > .description')
            item['description'] = ''.join(desc.xpath('text()').extract() + desc.css('span::text').extract())\
                    .replace(u'\u2026', '').replace('\n', '').replace(u'\xa0', '')

            yield item
