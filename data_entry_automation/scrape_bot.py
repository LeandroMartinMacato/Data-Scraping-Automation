from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://www.lamudi.com.ph/metro-manila/makati/apartment/rent/price:0-10000/bedrooms:1/"

HEADERS = ({'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",
            'Accept-Language': "en-US,en;q=0.9"})

class ScrapeBot:
    ''' Lamundi.com Rent Listing Scraper'''

    def __init__(self, SITE_URL):
        self.soup = self.start_soup(SITE_URL) 

    def start_soup(self , url):
        response = requests.get(url , headers = HEADERS)
        website = response.text
        soup = BeautifulSoup(website , "html.parser")

        return soup

    def scrape_listings(self):
        scrape_listings = [] 

        for listing in self.soup.find_all('div' , {'class': 'ListingCell-AllInfo ListingUnit'}):
            ''' for every listing '''
            list_name = listing.find('h2' , {'class': 'ListingCell-KeyInfo-title'})
            list_name = self.clean_string(list_name.text)

            list_link = listing.find('a' , {'class': 'js-listing-link'})
            list_link = self.clean_string(list_link['href'])

            list_price = listing.find('span' , {'class': 'PriceSection-FirstPrice'})
            list_price = self.clean_string(list_price.text)

            list_details = {
                "room_num" : "",
                "bath_num" : "",
                "floor_area" : ""
            }

            list_room_bath_size = listing.find_all('span' , {'class': 'KeyInformation-value_v2 KeyInformation-amenities-icon_v2'})


            details = []
            for detail in list_room_bath_size:
                detail_string = self.clean_string(detail.text)
                details.append(detail_string)

                try:
                    list_details["room_num"] = details[0]
                    list_details["bath_num"] = details[1]
                    list_details["floor_area"] = details[2]
                except Exception as e:
                    print(e)
                    list_details["floor_area"] = "n/a" 


            listings = {
                "list_name" : list_name,
                "list_link" : list_link,
                "list_price" : list_price,
                "list_details" : list_details
            }
            scrape_listings.append(listings)


        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~COMPLETE ALL SCRAPE~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return scrape_listings

    def clean_string(self , string):
        try:
            clean_string = string.strip()
            clean_string.replace(" ","")
            clean_string.replace("\n","")
            clean_string.replace("\n\n","")
            clean_string.replace("'\n\n","")
            clean_string.replace("'\n","")
            clean_string.replace("1\n","\n")
            clean_string.replace("...\n","")
        except Exception as e:
            print(e)
            print("String not cleanable")
            return string

        return clean_string




if __name__ == '__main__':
    scraper = ScrapeBot(URL)
    # scraper.scrape_listings()
    print(scraper.scrape_listings())