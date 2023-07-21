import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        links = response.css('section#numerical-index tbody tr a::attr(href)')
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get()
        pattern = r'PEP (?P<number>\d+)\W+(?P<name>.+)$'
        pep_number, pep_name = re.search(pattern, pep_title).groups()
        data = {
            'number': pep_number,
            'name': pep_name,
            'status': response.css(
                'dt:contains("Status") + dd'
            ).css('abbr::text').get()
        }
        yield PepParseItem(data)
