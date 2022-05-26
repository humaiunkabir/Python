from asyncore import write
import scrapy
import csv


class LinkbotSpider(scrapy.Spider):
    name = 'linkBot'
    allowed_domains = ['www.monsterindia.com']
    start_urls = ['https://www.monsterindia.com/search/jobs-by-skill']

    def parse(self, response):
        titles = response.xpath(
            '//*[@id="themeDefault"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div/div/ul/li/a/@title').getall()

        links = response.xpath(
            '//*[@id="themeDefault"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div/div/ul/li/a/@href').getall()

        data = [[titles[index], links[index]] for index in range(len(links))]

        # Save Into File

        with open('JobCatLinks.csv', mode='w', newline='') as file:
            writer=csv.writer(file, delimiter="|")
            writer.writerow(['Title', 'Job Links'])
            writer.writerows(data)