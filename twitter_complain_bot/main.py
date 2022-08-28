from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

SPEED_URL = "https://www.speedtest.net/"
TWIT_URL = "https://twitter.com/i/flow/login" 
TWIT_USER = "ENTER_YOUR_USER"
TWIT_PASS = "ENTER_YOUR_PASS"

ISP_TWITTER = "@Converge_CSU "
TRUE_SPEED = {
    "dl_speed" : 200,
    "up_speed" : 200
}
DEMO_CURR_SPEED = {
    "dl_speed" : 100,
    "up_speed" : 100
}

class SpeedBot:
    def __init__(self , url ):
        self.url = url
        self.driver = None

    def get_internet_speed(self):
        self.initialize_bot_driver()
        internet_speed = { "dl_speed" : " ", "up_speed":" "}
        start_test_button = self.driver.find_element_by_css_selector(".start-text")
        start_test_button.click()
        time.sleep(20)
        
        while internet_speed["dl_speed"] and internet_speed["up_speed"] == " ":
            internet_speed = {
                "dl_speed" : self.driver.find_element_by_css_selector(".download-speed").text,
                "up_speed" : self.driver.find_element_by_css_selector(".upload-speed").text
            }

        print(f"SPEED TEST COMPLETE \n results:{internet_speed}")
        self.driver.quit()
        return internet_speed

    def initialize_bot_driver(self):
        initialized_driver = webdriver.Edge()
        initialized_driver.get(self.url)
        print("SpeedBot Initialized..")

        self.driver = initialized_driver

class TwitterComplainBot:
    def __init__(self,url , promised_net_speed: dict):
        self.url = url
        self.driver = None
        self.true_net_speed = promised_net_speed
        self.will_complain = False

    def speed_check(self , curr_speed: dict):
        if float(curr_speed["dl_speed"]) <= self.true_net_speed["dl_speed"] and float(curr_speed["up_speed"]) <= self.true_net_speed["up_speed"]:
            print("🔺 MINIMUM SPEED FAILED , AUTOMATING TWEET COMPLAIN ")

            self.initialize_bot_driver()

            time.sleep(3)

            twit_login = self.driver.find_element_by_name("text")
            twit_login.click()
            twit_login.send_keys(TWIT_USER)
            twit_login.send_keys(Keys.ENTER)

            time.sleep(3)

            twit_password = self.driver.find_element_by_name("password")
            twit_password.click() 
            twit_password.send_keys(TWIT_PASS)
            twit_password.send_keys(Keys.ENTER)

            time.sleep(3)

            twit_type = self.driver.find_element_by_css_selector(".public-DraftStyleDefault-block")
            twit_type.click()
            twit_type.send_keys(f"[AUTOMATION] Hey {ISP_TWITTER}, why is my internet {curr_speed['dl_speed']} mbps download / {curr_speed['dl_speed']} upload when I pay for {self.true_net_speed['dl_speed']} mbps download / {self.true_net_speed['dl_speed']} upload speed ")

            twit_tweet_butt = self.driver.find_element_by_xpath('//div[@data-testid="tweetButtonInline"]')
            twit_tweet_butt.click() # ACTUAL TWEET BUTTON

        else:
            print("MINIMUM SPEED TEST SUCCESSFUL! No need to complain about 💃")


    def initialize_bot_driver(self):
        initialized_driver = webdriver.Edge()
        initialized_driver.get(self.url)
        print("SpeedBot Initialized..")

        self.driver = initialized_driver
        self.driver.maximize_window()


if __name__ == "__main__":
    speed_bot = SpeedBot(SPEED_URL) 
    twit_bot = TwitterComplainBot(TWIT_URL ,TRUE_SPEED )
    twit_bot.speed_check(speed_bot.get_internet_speed())


    while True:
        pass