from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test.pages.base_page import BasePage
from utilities.config import Config


class ProductPage(BasePage):

    page_logo = (By.XPATH, "(//div[@class='logo'])[2]")
    product_xpath = "//h5[normalize-space(text())='<product>']//following::button[1]"
    checkout_button = (By.XPATH, "(//span[@class='icon cart'])[2]")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def product_selection(self,product_name):
        WebDriverWait(self.driver, Config.wait_time).until(EC.presence_of_element_located(self.page_logo))
        text = self.product_xpath.replace('<product>',product_name)
        element = self.driver.find_element_by_xpath(str(text))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        action.click(element).perform()

    def click_checkout_btn(self):
        self.do_click(self.checkout_button)

