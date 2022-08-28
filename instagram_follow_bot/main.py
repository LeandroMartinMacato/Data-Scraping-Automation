from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

URL = "https://www.instagram.com/"
PAGE_URL = "https://www.instagram.com/pewdiepie/"
IG_USER = "YOUR_USERNAME"
IG_PASS = "YOUR_PASSWORD"

class IgFollowBot:
    def __init__(self , ig_url):
        self.url = ig_url
        self.driver = None


        
    def initialize_bot_driver(self):
                initialized_driver = webdriver.Edge()
                initialized_driver.get(self.url)
                print("SpeedBot Initialized..")

                self.driver = initialized_driver
                self.driver.maximize_window()

    def open_twitter(self):
        self.initialize_bot_driver()

    def login_twitter(self):
        ''' From login to home page '''
        self.driver.implicitly_wait(2)
        user = self.driver.find_element_by_name("username")
        user.click()
        user.send_keys(IG_USER)

        passwrd = self.driver.find_element_by_name("password")
        passwrd.click()
        passwrd.send_keys(IG_PASS)

        log_butt = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        log_butt.click()

        self.driver.implicitly_wait(5)
        dont_save_info_butt = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        dont_save_info_butt.click()

        self.driver.implicitly_wait(5)
        dont_on_notif_butt = self.driver.find_element_by_css_selector('._a9--._a9_1')
        dont_on_notif_butt.click()



    def search_page(self ,page):
        ''' from home page to page searched'''
        self.driver.implicitly_wait(2)

        search_bar = self.driver.find_element_by_xpath('//input[@aria-label="Search input"]')
        self.driver.execute_script("arguments[0].click();",search_bar)
        search_bar.send_keys(page)

        self.driver.implicitly_wait(2)


        first_search = self.driver.find_element_by_css_selector('.oajrlxb2')
        self.driver.execute_script("arguments[0].click();",first_search)


    def open_ig_page(self,page_url):
        ''' from anypage if logged in go to target ig page'''
        ig_page = self.driver.get(page_url)
        self.driver.forward() # change driver to next tab


    def follow_all_followers(self , follow_batch_size ):
        self.driver.implicitly_wait(5)
        print("wait complete...")

        follower_count = self.driver.find_element_by_css_selector('a.oajrlxb2.g5ia77u1.qu0x051f')
        follower_count.click()

        batch = 0 
        while batch < follow_batch_size:
            try:
                ''' try every follow button '''
                for follower in self.driver.find_elements_by_css_selector('._acan._acap._acas'):
                    follower.click()
            except Exception as e:
                print(f"EXCEPTION: {e}\nLoading new follow list... ")

            try:
                ''' try to cancel unfollow prompt  '''
                cancel_unfollow_butt = self.driver.find_element_by_css_selector('button._a9--._a9_1')
                cancel_unfollow_butt.click()
            except NoSuchElementException:
                print("No overlay cancel")




            batch += 1
            self.driver.implicitly_wait(3)

        print("Auto Follow Automation Complete")




if __name__ == "__main__":
    ig_bot = IgFollowBot(URL)
    ig_bot.open_twitter()
    ig_bot.login_twitter()
    # ig_bot.search_page("pewdiepie")
    ig_bot.open_ig_page(PAGE_URL)
    ig_bot.follow_all_followers(3)


    while True:
        pass