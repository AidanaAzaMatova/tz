import scrapy
#с какой целью я импортировала
import dateparser

class TengriSpider(scrapy.Spider):
    name = "tengri"
    start_urls = [
        "https://tengrinews.kz/",
    ]

    def parse(self, response):
        for tengri in response.css("div.main-news_super_item"):
            yield {
                "title": tengri.css("span.main-news_super_item_title a::text").get(),
                "date": tengri.css("div.main-news_super_item_meta time::text").get(),
                "link": "https://tengrinews.kz"+tengri.css("span.main-news_super_item_title a::attr(href)").get()

            }



class NurSpider(scrapy.Spider):
    name = "nur"
    start_urls = [
        "https://nur.kz/",
    ]

    def parse(self, response):
        for nur in response.css("li.block-top-hero__item"):
            yield {
                "title": nur.css("a.js-article-link::text").get(),
                "date": nur.css("time.preview-info-item-secondary::text").get(),
                "link": nur.css("h3.preview-title a::attr(href)").get()

            }

class ScientificSpider(scrapy.Spider):
    name = "scinetific"
    start_urls = [
        "https://scientificrussia.ru/",
    ]




    def parse(self, response):
        for nur in response.css("div.list-item"):
            yield {
                "title": nur.css("div.title a::text").get(),
                "date": nur.css("div.prop time::text").get(),
                "link": "https://scientificrussia.ru/"+nur.css("div.title a::attr(href)").get()

            }