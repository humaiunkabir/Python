import scrapy
import csv


class LinkbotSpider(scrapy.Spider):
    name = 'linkBot'
    allowed_domains = ['www.squarehospital.com']
    start_urls = ['https://www.squarehospital.com/departments']

    def parse(self, response):
        titles = response.xpath('/html/body/section[1]/div/div[2]/div/div/div/div/ul/li/a/text()').getall()
        links = response.xpath('/html/body/section[1]/div/div[2]/div/div/div/div/ul/li/a/@href').getall()

        data = [[titles[index], links[index]] for index in range(len(titles))]    

        with open('HospitalDepLinks.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow(['Deppartment Title', 'Links'])
            writer.writerows(data)