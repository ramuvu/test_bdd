from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from assertpy import assert_that

from test.pages.base_page import BasePage

class CheckOutPage(BasePage):

    product_text = (By.XPATH, "//li[@class='ng-star-inserted']//div[@class='_left']//h5")
    product_total = (By.XPATH, "(//p[normalize-space(text()) = 'Total'])[1]//following::p[1]")
    product_payable = (By.XPATH, "(//b[normalize-space(text()) = 'Total Payable'])[1]//following::b[1]")

    def __init__(self,driver):
        super().__init__(driver)

    def verify_product_txt(self,exp_text):
        act_text = self.get_element_text(self.product_text)
        assert act_text == exp_text

    def verify_product_total(self,exp_total,exp_payable):
        act_total = self.get_element_text(self.product_total)
        act_payable = self.get_element_text(self.product_payable)
        assert_that(act_total).contains(exp_total)
        assert_that(act_payable).contains(exp_payable)