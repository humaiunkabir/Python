import scrapy
import csv
from ..items import HospitaldatascraperItem


class DepspiderSpider(scrapy.Spider):
    name = 'DepSpider'
    allowed_domains = ['www.squarehospital.com']
    with open("G:\HR_Venture_Python_Django_Training\ProjectAll\Python\HospitalDataScraping\HospitalDataScraper\HospitalDepLinks.csv") as file:
        reader = csv.reader(file,delimiter="|")
        links = [row[1] for row in reader]
    start_urls = links[1:]
    

    def parse(self, response):
        doctornames = response.xpath(
            '/html/body/section[1]/div/div[2]/div/div/div/div/div/div[2]/h3').getall()
        doctornames = list(map(lambda name: name.replace(
            '<h3>', '').replace('</h3>', '') if name else name, doctornames))

        specilities = response.xpath(
            '/html/body/section[1]/div/div[2]/div/div/div/div/div/div[2]/p').getall()
        specialitiesAndDegree = list(map(lambda spe: spe.replace('<p>', '').replace('</p>', '').replace('\n', '').replace(
            '<strong>', '').replace('</strong>', '').replace('<br>', '').strip() if spe else spe, specilities))
        specialitiesAndDegree = list(map(lambda spe: spe.partition(
            'Degree - ') if spe else spe, specialitiesAndDegree))
        SpecialityList = list(map(lambda item: item[0].strip().replace(
            'Specialty - ', ''), specialitiesAndDegree))
        DegreeList = list(map(lambda item: item[2], specialitiesAndDegree))
        doctorDetailsLinks = response.xpath(
            '/html/body/section/div/div/div/div/div/div/div/div/div/a[3]/@href').getall()
        
        departmentList = []
        department = response.xpath('/html/body/section[1]/div/div[1]/div/div/div[1]/h2/text()').get() 
        for index in range(len(doctornames)):
            departmentList.append(department)

        # data = [[doctornames[index], SpecialityList[index], DegreeList[index], doctorDetailsLinks[index]] for index in range(len(doctornames))]

        # with open('DoctorsList.csv', mode='w', newline='') as file:
        #     writer = csv.writer(file, delimiter='|')
        #     writer.writerow(['DoctorName', 'Speciality', 'Degree', 'DetailsLink'])
        #     writer.writerows(data)

        obj = HospitaldatascraperItem()
        obj['doctorName'], obj['speciality'], obj['degree'], obj['doctorDetailsLink'], obj['department'] = doctornames, SpecialityList, DegreeList, doctorDetailsLinks, departmentList
                #response.follow(doctorDetailsLinks[index], self.parse_additional_page, cb_kwargs=dict(obj=obj))
        yield obj

        # def parse_additional_page(self, response, obj):
        #     doctorDetails = response.xpath(
        #         '/html/body/section/div/div[2]/div/div/div/div[3]/p').getall()
        #     doctorDetails = list(map(lambda item: item.replace(
        #         '<p>', '').replace('<p class="mar-30">\n', ''), doctorDetails))
        #     doctorDetails = list(map(lambda item: item.replace('<p>', '').replace(
        #         '</p>', '').replace('<br>', ''), doctorDetails))
        #     obj['doctorDetails'] = doctorDetails[1] + \
        #         doctorDetails[2]+doctorDetails[3]
        #     return obj
