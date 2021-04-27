from selenium.webdriver.common.by import By


class Techlistlocators():

    first_name = (By.XPATH,"//input[@name = 'firstname']")
    lastname = (By.NAME,"lastname")
    gender = (By.ID,"sex-0")
    experiance = (By.ID,"exp-2")
    dateofbirth = (By.ID,"datepicker")
    profession = (By.ID,"profession-1")
    tool = (By.ID,"tool-2")
    country = (By.ID,"continents")
    selenium_command = (By.ID,"selenium_commands")
    upload_photo = (By.ID,"photo")
    submit_button = (By.ID,"submit")