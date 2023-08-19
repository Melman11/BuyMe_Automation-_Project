import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
from login_page import LoginPage
from home_screen import HomeScreen
from pick_business import PickBusiness
from sender_receiver_info import SenderReceiver


@pytest.fixture
def setUp():
    # opens json file
    json_file = open('config.json', 'r')
    data = json.load(json_file)
    # chooses browser type
    browser = data['browserType']
    if browser == 'chrome':
        driver = webdriver.Chrome(
            service=Service("C:\\Users\\nivis\\Downloads\\chromedriver-win64\\chromedriver-win64.exe"))
    elif browser == 'firefox':
        pass
        # driver = webdriver.Firefox(service=Service('FIREFOXDRIVER_PATH'))
    # opens the webpage based on the json
    url = data['URL']
    driver.get(url)
    # implicit wait
    driver.implicitly_wait(10)
    # page load timeout
    driver.set_page_load_timeout(10)
    yield driver
    driver.quit()


def test_login_page(setUp):
    driver = setUp
    login_test = LoginPage(driver)
    login_test.enter_credentials()


def test_home_screen(setUp):
    driver = setUp
    home_screen = HomeScreen(driver)
    home_screen.set_price()
    home_screen.set_area()
    home_screen.set_category()
    home_screen.search()


def test_pick_business(setUp):
    driver = setUp
    site_url = driver.current_url
    desired_url = "https://buyme.co.il/search?budget=3&category=419&region=13"
    assert site_url == desired_url
    pick_business = PickBusiness(driver)
    pick_business.select_business()
    pick_business.enter_amount()


def test_sender_receiver_info(setUp):
    driver = setUp
    sender_receiver_info = SenderReceiver(driver)
    sender_receiver_info.gift_receiver()
    sender_receiver_info.upload_picture()
