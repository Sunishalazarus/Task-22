from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class GuviInstagram:

    def __init__(self, url="https://www.instagram.com/guviofficial/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        This method is to open up the chrome browser with the URL and makes the browser to go fullscreen.
        """
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def quit(self):
        """
        This method is used to close the webbrowser
        """
        self.driver.quit()

    def findElementByXPath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def get_followers_following(self):
        """
        To get the total number of followers and following from the given url.
        :return:
        """
        try:
            self.boot()
            sleep(5)
            followers_element = self.findElementByXPath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span")
            print("Total followers:", followers_element.text)
            sleep(3)
            following_element = self.findElementByXPath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span")
            print("Total following:", following_element.text)
            sleep(3)

        except NoSuchElementException as e:
            print("Error", e)
        finally:
            self.quit()

obj= GuviInstagram()
obj.get_followers_following()

"""
Output-
Total followers: 147K
Total following: 6
"""


