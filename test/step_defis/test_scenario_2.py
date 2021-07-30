import pytest
from pytest_bdd import scenario,scenarios,given,when,then,parser

from test.pages.checkout_page import CheckOutPage
from test.pages.home_page import HomePage
from test.pages.product_page import ProductPage
from test.step_defis.test_base_test import BaseTest
import time

urbankissan_home = "https://www.urbankisaan.com/"

scenarios('C:/Users/Rambabu/PycharmProjects/python_bdd_1/test/features/scenario2.feature')

@given('The urbankissan home page displayed')
def test_home_page(init_driver):
    home_page = HomePage(init_driver)
    home_page.launch_browser(urbankissan_home)

@when('The user click on Shop now')
def test_click_shop(init_driver):
    home_page = HomePage(init_driver)
    home_page.click_shop_now()

@when('The user selects multiple products and add to basket')
def test_select_product(init_driver):
    product_page = ProductPage(init_driver)
    product_page.product_selection("Banana G9")
    product_page.product_selection("Sapota")
    product_page.product_selection("Indian Guava")
    product_page.product_selection("Green Apple")

@when('The user clicks checkout button')
def test_click_checkout_button(init_driver):
    product_page = ProductPage(init_driver)
    product_page.click_checkout_btn()


@then('The user can able to see products list in checkout page')
def test_verify_product(init_driver):
    checkout = CheckOutPage(init_driver)
    checkout.verify_product_total("259","289")

