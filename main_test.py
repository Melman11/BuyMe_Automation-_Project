import logging
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
from login_page import LoginPage
from home_screen import HomeScreen
from pick_business import PickBusiness
from sender_receiver_info import SenderReceiver

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="selenium_log.log"
)


@pytest.fixture(scope="class")
def driver_setup(request):
    logging.info("Setting up driver...")
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
    driver.implicitly_wait(10)
    # page load timeout
    driver.set_page_load_timeout(15)
    # maximize the browser window
    driver.maximize_window()
    # make the driver instance available for the test functions
    request.cls.driver = driver
    # opens the webpage based on the json
    url = data['URL']
    driver.get(url)
    logging.info("Driver setup completed")
    yield

    logging.info("Closing driver...")
    driver.quit()
    logging.info("Driver closed")


@pytest.mark.usefixtures("driver_setup")
class TestYourWebsiteTests:
    def test_login_page(self):
        try:
            logging.info("Starting test_login_page")
            login_test = LoginPage(self.driver)
            login_test.enter_credentials()
            logging.info("test_login_page completed successfully")
        except:
            logging.error(f"An error occurred during test_login_page")

    def test_home_screen(self):
        try:
            logging.info("Starting test_home_screen")
            home_screen = HomeScreen(self.driver)
            home_screen.set_price()
            home_screen.set_area()
            home_screen.set_category()
            home_screen.search()
            logging.info("test_home_screen completed successfully")
        except:
            logging.error(f"An error occurred during test_home_screen")

    def test_pick_business(self):
        try:
            logging.info("Starting test_pick_business")
            site_url = self.driver.current_url
            desired_url = "https://buyme.co.il/search?budget=3&category=419&region=13"
            assert site_url == desired_url
            pick_business = PickBusiness(self.driver)
            pick_business.select_business()
            pick_business.enter_amount()
            logging.info("test_pick_business completed successfully")
        except:
            logging.error(f"An error occurred during test_pick_business")

    def test_sender_receiver_info(self):
        try:
            logging.info("Starting test_sender_receiver_info")
            sender_receiver_info = SenderReceiver(self.driver)
            sender_receiver_info.gift_receiver()
            sender_receiver_info.upload_picture()
            sender_receiver_info.enter_email()
            logging.info("test_sender_receiver_info completed successfully")
        except:
            logging.error(f"An error occurred during test_sender_receiver_info")
