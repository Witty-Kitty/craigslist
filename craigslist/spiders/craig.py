from scrapy.spiders import Spider
from scrapy import Selector
from craigslist.items import CraigsList



class MySpider(Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo/"]

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath("//p//a[@class='result-title hdrlnk']")
        items = []
        for titles in titles:
            item = CraigsList()
            item["title"] = titles.select("text()").extract()
            item["link"] = titles.select("@href").extract()
            items.append(item)
        return items