from selenium import webdriver

import time

URL = "https://forms.gle/zCS9NjbWApEqbvbSA"

DEBUG_DATA = [
  {
    'list_name': 'For Rent: MyTown Athens Corporate Staff Housing with Condo-style Amenities in Cembo, ...',
    'list_link': 'https://www.lamudi.com.ph/for-rent-mytown-athens-corporate-staff-housing-with-condo-style-amenities-in-cembo-makati-near-uptown-bgc.html',
    'list_price': '₱ 4,400',
    'list_details': {
      'room_num': '1',
      'bath_num': '1',
      'floor_area': 'n/a'
    }
  },
  {
    'list_name': 'For Rent: MyTown New York 2-Bed Sharing Furnished Unit in Guadalupe Nuevo, Makati | n...',
    'list_link': 'https://www.lamudi.com.ph/for-rent-mytown-new-york-2-bed-sharing-furnished-unit-in-guadalupe-nuevo-makati-near-32nd-st-bgc-makati-cbd.html',
    'list_price': '₱ 8,870',
    'list_details': {
      'room_num': '1',
      'bath_num': '1',
      'floor_area': 'n/a'
    }
  }
]

class FormBot:
    def __init__(self , form_url):
        self.url = form_url
        self.driver = None

    def fill_form(self , data ):
        for cnt , form in enumerate(self.driver.find_elements_by_css_selector(".whsOnd.zHQkBf")):
            form.click()
            try:
                if cnt == 0:
                    form.send_keys(data["list_name"])
                elif cnt == 1:
                    form.send_keys(data["list_link"])
                elif cnt == 2:
                    form.send_keys(data["list_price"])
                elif cnt == 3:
                    form.send_keys(data["list_details"]["room_num"])
                elif cnt == 4:
                    form.send_keys(data["list_details"]["bath_num"])
                elif cnt == 5:
                    form.send_keys(data["list_details"]["floor_area"])
            except Exception as e:
                print(f"EXCEPTION: {e}\n Element not visible BUG")
                #TODO: FIX EXCEPTION BUG

            

    def submit_form(self):
        submit_butt = self.driver.find_element_by_css_selector(".NPEfkd.RveJvd.snByac")
        submit_butt.click()
        
    def initialize_bot_driver(self):
                # options = Options()
                # options.add_argument("--window-size=1200x600")
                # initialized_driver = webdriver.Edge(options)

                initialized_driver = webdriver.Edge()
                initialized_driver.get(self.url)
                print("Formbot Initialized..")

                self.driver = initialized_driver
                self.driver.implicitly_wait(2)

    def open_form(self):
        self.initialize_bot_driver()

if __name__ == '__main__':
    form_bot = FormBot(URL) 
    form_bot.initialize_bot_driver()
    form_bot.fill_form(DEBUG_DATA[0])
    # form_bot.submit_form()


    while True:
        pass
