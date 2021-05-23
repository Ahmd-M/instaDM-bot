from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
#from loginInfo import myUser, myPassword

#Your Login Information
myUser = ''
myPasword =  ''

PATH = '' #Path for your "chromedriver.exe" file
driver = webdriver.Chrome(PATH)

users = []    #Enter username of the message receiver
message_ = ()  #Enter the message

  
class bot:
    def __init__(self, username, password, users, message):
        self.username = username
        self.password = password
        self.users = users
        self.message = message
        self.url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()
    
    
    def wait_driver(self,method,value,duration):
        if method.upper() == "NAME":
            element = WebDriverWait(self.bot, duration).until(
            expected_conditions.presence_of_element_located((By.NAME, value)))
        else:
            element =  WebDriverWait(self.bot, duration).until(
            expected_conditions.presence_of_element_located((By.XPATH, value)))
        return element


    def login(self):
        self.bot.get(self.url)
  
        enter_username = self.wait_driver("name","username",20)
        enter_password = self.wait_driver("name","password",20)

        enter_username.send_keys(self.username)
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)

        #First pop-up
        self.wait_driver("xpath",'//*[@id="react-root"]/section/main/div/div/div/div/button',20).click()

        #Second pop-up
        self.wait_driver("xpath",'/html/body/div[4]/div/div/div/div[3]/button[2]',20).click()

        #Clicking Direct button
        self.wait_driver("xpath",'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a',20).click()

        #Clicking on pencil icon
        self.wait_driver("xpath",'//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button',20).click()


        time.sleep(2)
        for user in self.users:

            #Entering the username
            self.wait_driver("xpath",'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input',20).send_keys(user)
            
            #Clicking on the username
            self.wait_driver("xpath",'/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button',20).click()
            
            #Clicking "Next" button
            self.wait_driver("xpath",'/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div',20).click()
            
            #Clicking on message area
            send = self.wait_driver("xpath",'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea',20)

            #Typing the message
            send.send_keys(self.message)
            time.sleep(1)
  
            #Sending the message
            send.send_keys(Keys.RETURN)

            time.sleep(2)
            
            #Closing the tab
            #self.bot.quit()
  
           
  

def run():
    bot(myUser, myPassword, users, message_)

run()
