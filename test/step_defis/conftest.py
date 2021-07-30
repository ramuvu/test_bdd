import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def init_driver():
    driver = webdriver.Chrome(executable_path='C:/Users/Rambabu/Downloads/chromedriver_win32 (1)/chromedriver.exe')
    #request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.close()