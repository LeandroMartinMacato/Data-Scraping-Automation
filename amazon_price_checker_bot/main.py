from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

ITEM_URL = "https://www.amazon.com/Fuel-Rollin-Sparkly-Inspired-Servings/dp/B09XTMB3ZR/ref=sr_1_1?crid=3K1CV97URZJK6&keywords=gfuel&qid=1653893102&sprefix=gfue%2Caps%2C272&sr=8-1https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

HEADERS = ({'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",
            'Accept-Language': "en-US,en;q=0.9"})


class smtp_bot():
    def __init__(self , my_email , my_password):
        self.my_email = my_email
        self.my_password = my_password
        self.send_to_email = ""
        self.message = """
            From: From Person <from@fromdomain.com>
            To: To Person <to@todomain.com>
            Subject: SMTP e-mail test

            This is a test e-mail message.
            """

    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
                connection.starttls()  # Make connection secure
                connection.login(user=self.my_email, password=self.my_password)
                connection.sendmail(from_addr=self.my_email,
                                    to_addrs=self.send_to_email,
                                    msg= self.message)

    def set_message(self, message):
        self.message = message

    def set_email_to(self, email_to):
        self.send_to_email = email_to




def main():
    TARGET_PRICE = 30.00
    response = requests.get(ITEM_URL , headers = HEADERS)

    website = response.text # HTML

    soup = BeautifulSoup(website , "lxml")

    #name
    product_name_element = soup.find("span" , {"id" : "productTitle"})
    product_name = product_name_element.get_text()

    #price
    price_element = soup.find(name = "span" , class_ = "a-offscreen")
    price = price_element.get_text()
    price = float(price.replace("$",""))


    email_bot = smtp_bot("shadowgoreo@gmail.com","ENTER PASSWORD HERE")
    email_bot.set_email_to("shadowslayerhero@gmail.com")
    email_bot.set_message(f""" 
        PRICE ALERT!
        Your item {product_name} is on your target price of {TARGET_PRICE} and is currently {price} today !
    
    """)
    
    print(product_name)
    print(price)

    if price < TARGET_PRICE:
        try:
            email_bot.send_email()
            print("SENT EMAIL")
        except Exception as e:
            print(f"EXCEPTION: {e}")
            print("Error sending email")




if __name__ == "__main__":
    main()