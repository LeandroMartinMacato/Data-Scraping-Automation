from scrape_bot import ScrapeBot
from form_bot import FormBot

import time

SCRAPE_URL = "https://www.lamudi.com.ph/metro-manila/makati/apartment/rent/price:0-10000/bedrooms:1/"
FORM_URL = "https://forms.gle/zCS9NjbWApEqbvbSA"

if __name__ == '__main__':
    # Scrape Data
    scraper = ScrapeBot(SCRAPE_URL)
    scraped_data = scraper.scrape_listings()

    # Automate Form
    for data in scraped_data:
        form_bot = FormBot(FORM_URL) 
        form_bot.initialize_bot_driver()
        form_bot.fill_form(data)
        form_bot.submit_form()

    print("AUTOMATION COMPLETE 🎉")




