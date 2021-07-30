import pytest
from pytest_bdd import scenario,scenarios,given,when,then,parser
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


# url "
urbankissan_home = "https://www.urbankisaan.com/"

scenarios('C:/Users/Rambabu/PycharmProjects/python_bdd_1/test/features/web.feature')

# fixture
@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path='C:/Users/Rambabu/Downloads/chromedriver_win32 (1)/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


# Given steps

@given('the urbankissan home page displayed',target_fixture='home_page')
def home_page(browser):
    browser.get(urbankissan_home)

@when('the user click on Shop now button')
def click_shop_now(browser):
    shop_btn = browser.find_element_by_xpath("(//a[@href='/shop'])[1]")
    shop_btn.click()

@when('the user selects products to add')
def select_product(browser):
    WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"(//div[@class='logo'])[2]")))
    element = browser.find_element_by_xpath("//h5[normalize-space(text())='Banana G9']//following::button[1]")
    time.sleep(3)
    #browser.execute_script("argument[0].scrollIntoView(false);",element)
    action = ActionChains(browser)
    action.move_to_element(element).perform()
    element.click()

@when('the user click checkout button')
def click_checkout_button(browser):
    element = browser.find_element_by_xpath("//button[@class='btn btn-violet cust_checkout ng-star-inserted']")
    element.click()

@then('the user can able to see product in checkout page')
def verify_product(browser):
    time.sleep(10)
    element = browser.find_element_by_xpath("//li[@class='ng-star-inserted']//div[@class='_left']//h5")
    act_value = element.get_attribute('innerText')
    assert act_value == "Banana G9"



