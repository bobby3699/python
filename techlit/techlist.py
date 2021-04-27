from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import logging
import time
from techlocators import Techlistlocators

class Techlist:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def login(self):
        logging.basicConfig(level=logging.INFO)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(5)
        self.driver.find_element(*Techlistlocators.first_name).send_keys("bobby")
        logging.info("successfully entered first name")
        self.driver.find_element(*Techlistlocators.lastname).send_keys("korimella")
        logging.info("successful entered last name")
        self.driver.find_element(*Techlistlocators.gender).click()
        logging.info("successfully select the gender")
        self.driver.find_element(*Techlistlocators.experiance).click()
        logging.info("successfully select the experience")
        self.driver.find_element(*Techlistlocators.dateofbirth).send_keys("01/10/1995")
        logging.info("enter date of birth successfully")
        self.driver.find_element(*Techlistlocators.profession).click()
        logging.info("successfully select the profession")
        self.driver.find_element(*Techlistlocators.tool).click()
        logging.info("successfully select the tool")
        Select(self.driver.find_element(*Techlistlocators.country)).select_by_visible_text("Asia")
        logging.info("successfully select county")
        Select(self.driver.find_element(*Techlistlocators.selenium_command)).select_by_visible_text("Browser Commands")
        logging.info("successfully select the selenium commands")
        self.driver.execute_script("window.scrollTo(0, 1200)")
        self.driver.find_element(*Techlistlocators.upload_photo).send_keys("//home//bobby//Pictures//garuda_linux.png")
        logging.info("successfully upload the profile photo")
        #self.driver.find_element_by_id(*Techlistlocators.submit_button).click()
        logging.info("login successfully")


        time.sleep(10)
        self.driver.close()


if __name__ == "__main__":
    tech = Techlist()
    tech.login()