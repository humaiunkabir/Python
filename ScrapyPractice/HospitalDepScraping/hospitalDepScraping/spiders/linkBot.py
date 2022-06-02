import scrapy
import csv


class LinkbotSpider(scrapy.Spider):
    name = 'linkBot'
    allowed_domains = ['www.squarehospital.com']
    start_urls = ['https://www.squarehospital.com/departments']

    def parse(self, response):
         
        links = response.xpath(
            '/html/body/section[1]/div/div[2]/div/div/div/div/ul/li/a/@href').getall()
            

        data = [[links[index].rsplit('/', 1)[-1], links[index]] for index in range(len(links))]
        print(data)
        # Save into file

        with open('DepartmentCatLinks.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter="|")
            writer.writerow(['Title', 'Link'])
            writer.writerows(data)