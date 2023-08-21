import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
from login_page import LoginPage
from home_screen import HomeScreen
from pick_business import PickBusiness
from sender_receiver_info import SenderReceiver


@pytest.fixture(scope="class")
def driver_setup(request):
    # opens json file
    json_file = open('config.json', 'r')
    data = json.load(json_file)
    # chooses browser type
    browser = data['browserType']
    if browser == 'chrome':
        driver = webdriver.Chrome(
            service=Service("C:\\Users\\nivis\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"))
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            service=Service("C:\\Users\\nivis\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe"))
    # implicit wait
    driver.implicitly_wait(5)
    # page load timeout
    driver.set_page_load_timeout(8)
    # maximize the browser window
    driver.maximize_window()
    # make the driver instance available for the test functions
    request.cls.driver = driver
    # opens the webpage based on the json
    url = data['URL']
    driver.get(url)
    yield
    driver.quit()


@pytest.mark.usefixtures("driver_setup")
class TestYourWebsiteTests:
    def test_login_page(self):
        login_test = LoginPage(self.driver)
        login_test.enter_credentials()

    def test_home_screen(self):
        home_screen = HomeScreen(self.driver)
        home_screen.set_price()
        home_screen.set_area()
        home_screen.set_category()
        home_screen.search()

    def test_pick_business(self):
        site_url = self.driver.current_url
        desired_url = "https://buyme.co.il/search?budget=3&category=419&region=13"
        assert site_url == desired_url
        pick_business = PickBusiness(self.driver)
        pick_business.select_business()
        pick_business.enter_amount()

    def test_sender_receiver_info(self):
        sender_receiver_info = SenderReceiver(self.driver)
        sender_receiver_info.gift_receiver()
        sender_receiver_info.upload_picture()
        sender_receiver_info.enter_email()
