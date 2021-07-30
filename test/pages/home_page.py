from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage

class HomePage(BasePage):

    shop_now_button = (By.XPATH, "(//a[@href='/shop'])[1]")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def launch_browser(self,url):
        self.driver.get(url)

    def click_shop_now(self):
        self.do_click(self.shop_now_button)



