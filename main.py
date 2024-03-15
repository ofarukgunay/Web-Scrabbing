from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from users import username,password,search
import time

class Twitter:
    
    # path = "C:/Users/mehme/OneDrive/Masaüstü/ChromeDriver/chromedriver-win64/chromedriver.exe"
    
    def __init__(self,username,password,search):
        self.username = username
        self.password = password
        self.search = search
        self.browser = webdriver.Chrome()
        
    def signInUsername(self):
        self.browser.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoidHIifQ%3D%3D%22%7D")
        time.sleep(5)
        
        usernameInput = self.browser.find_element(By.TAG_NAME,"input")
        
        
        usernameInput.send_keys(username)
        usernameInput.send_keys(Keys.ENTER)
        
        time.sleep(5)
    
        
    def signInPassword(self):
        time.sleep(5)
        passwordInput = self.browser.find_element(By.NAME,"password")
        
        passwordInput.send_keys(password)
        
        time.sleep(5)
        
        passwordInput.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
    def clickExplore(self):
        self.browser.get("https://twitter.com/explore")
        time.sleep(5)
    
    def clickOmerGunay(self):
        time.sleep(3)
        gunayInput = self.browser.find_element(By.TAG_NAME,"input")
        
        gunayInput.send_keys(search)
        time.sleep(5)
        
        gunayInput.send_keys(Keys.ENTER)
        
        time.sleep(5)

    def countDiv(self):
        
        name=self.browser.find_elements(By.XPATH,"(//*[contains(@class,'css-175oi2r r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l')])")   # css-175oi2r r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l

        for value in name:
            print(value.text + "\n")
        
        time.sleep(5)
        
app = Twitter(username,password,search)

app.signInUsername()

app.signInPassword()

app.clickExplore()

app.clickOmerGunay()

app.countDiv()