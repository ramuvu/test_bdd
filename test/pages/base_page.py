from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config import Config


class BasePage:

    def __init__(self,driver):
        self.driver = driver


    def do_click(self,by_locator):
        element = WebDriverWait(self.driver,Config.wait_time).until(EC.visibility_of_element_located(by_locator))
        element.click()

    def do_send_keys(self,by_locator,text):
        element = WebDriverWait(self.driver,Config.wait_time).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(text)

    def get_element_text(self,by_locator):
        element = WebDriverWait(self.driver,Config.wait_time).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute('innerText')

    def is_enebled(self,by_locator):
        element = WebDriverWait(self.driver,Config.wait_time).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self,title):
        WebDriverWait(self.driver,Config.wait_time).until(EC.title_is(title))
        return self.driver.title
