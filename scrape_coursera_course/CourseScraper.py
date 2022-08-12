from bs4 import BeautifulSoup
import requests
import lxml
import json
import csv

URL = "https://www.coursera.org"
CATEGORIES = [
    "data-science", "computer-science", "business", "personal-development" , "information-technology" , "math-and-logic" , "physical-science-and-engineering" , "health" , "social-sciences" , "arts-and-humanities"
]
HEADERS = ({
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",
    'Accept-Language': "en-US,en;q=0.9"
})


class CourseraScraper:

    def __init__(self):
        self.response = ""
        self.dom = ""
        self.soup = ""
        self.courses_links = []
        self.scrapedData = []
        self.category = ""

    def setSite(self, complete_url):
        self.response = requests.get(complete_url, headers=HEADERS)
        self.dom = self.response.text  # HTML
        self.soup = BeautifulSoup(self.dom, "html.parser")

    def setCategory(self, course_category):
        self.category = course_category

    def getCoursesLink(self):
        self.setSite(URL + "/browse/" + self.category)

        courses = self.soup.find_all(name="a", class_="CardText-link")

        for course in courses:  # get all links of courses
            self.courses_links.append(URL + course.get("href"))

    def getScrapedData(self):
        scraped_data = []
        id = 0
        for link in self.courses_links:
            print(f"{id + 1}: Scraping {link}")
            self.setSite(link)
            id += 1

            course_name = self.soup.find(name="h1",
                                         class_="banner-title").get_text()

            try:
                course_provider = self.soup.select_one(
                    'div._2lnij6').get_text()

            except:
                course_provider = self.soup.select_one(
                    'h3.rc-Partner__title').get_text()

            try:
                course_description = self.soup.select_one(
                    '#main > div > div.rc-XdpSection.cdp-about > div > div > div > div._1b7vhsnq.m-t-2 > div.m-t-1.description > div > div'
                ).get_text()
            except:
                course_description = self.soup.select_one(
                    '#main > div > div:nth-child(2) > div > div > div > div._1b7vhsnq.m-t-2 > div.m-t-1.m-b-3.description > div'
                ).get_text()

            try:
                course_number_enrolled = self.soup.select_one(
                    'strong > span').get_text()
            except:  #
                course_number_enrolled = "N/A"

            try:
                course_number_ratings = self.soup.select_one(
                    '#main > div._iul6hq > div > div > div.rc-RatingLink > ul > li > a > div > div._wmgtrl9.m-r-1s.color-white > span > span'
                ).get_text()
            except:
                course_number_ratings = self.soup.select_one(
                    'div.rc-ProductMetrics').get_text()
            course_number_ratings = course_number_ratings.split()[0]

            course_name = course_name.encode("ascii", "ignore")
            course_provider = course_provider.encode("ascii", "ignore")
            course_description = course_description.encode("ascii", "ignore")
            course_number_enrolled = course_number_enrolled.encode(
                "ascii", "ignore")
            course_number_ratings = course_number_ratings.encode(
                "ascii", "ignore")

            course_name = course_name.decode().replace("\n", "")
            course_provider = course_provider.decode().replace("\n", "")
            course_description = course_description.decode().replace("\n", "")
            course_number_enrolled = course_number_enrolled.decode().replace(
                "\n", "")
            course_number_ratings = course_number_ratings.decode().replace(
                "\n", "")

            scraped_data.append({
                'id': id,
                'url': link,
                'name': course_name,
                'provider': course_provider,
                'description': course_description,
                'enrolled': course_number_enrolled,
                'ratings': course_number_ratings
            })

        self.scrapedData = scraped_data

    def save2CSV(self):
        csv_headers = [
            "id", "url", "Category Name", "Course Name",
            "Instructor/ Provider Name", "Course Description",
            "# of Students Enrolled", "# of Ratings"
        ]

        with open('courses.csv', 'w', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow(csv_headers)
            for course in self.scrapedData:
                row = [
                    course["id"], course["url"], self.category, course["name"],
                    course["provider"], course["description"],
                    course["enrolled"], course["ratings"]
                ]
                writer.writerow(row)
        print("COMPLETE: Saving to csv")


if __name__ == '__main__':
    print("Coursera Course Scraper")
    print("Enter a course category from the selection")
    print(CATEGORIES)
    category = input(":")
    
    Scraper = CourseraScraper()
    # Scraper.setCategory("business")
    Scraper.setCategory(category)
    Scraper.getCoursesLink()
    Scraper.getScrapedData()
    Scraper.save2CSV()

