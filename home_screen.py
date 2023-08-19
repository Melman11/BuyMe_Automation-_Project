from seleniumpagefactory.Pagefactory import PageFactory
import allure
from allure_commons.types import AttachmentType


# This class holds all the functions for the home screen
class HomeScreen(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    # locators for the webelements in the login
    locators = {
        'PriceDropDown': ('XPATH', '//*[@id="ember1053"]/div/div[1]/span'),
        'AreaDropDown': ('XPATH', '//*[@id="ember1088"]/div/div[1]/span'),
        'CategoryDropDown': ('XPATH', '//*[@id="ember1120"]/div/div[1]/span'),
        'PriceRange': ('XPATH', '//*[@id="ember1077"]/span'),
        'Area': ('XPATH', '//*[@id="ember1207"]'),
        'Category': ('XPATH', '//*[@id="ember1268"]'),
        'Search': ('XPATH', '//*[@id="ember1295"]')
    }

    # this function adds an allure report screenshot as an exception for every click_button() command
    def safe_click(self, element, screenshot_name):
        try:
            element.click_button()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=AttachmentType.PNG)

    # choose desired price from the dropdown
    def set_price(self):
        self.safe_click(self.PriceDropDown, "PriceDropDownScreenshot")
        self.safe_click(self.PriceRange, "PriceRangeScreenshot")

    # set desired area from the dropdown
    def set_area(self):
        self.safe_click(self.AreaDropDown, "AreaDropDownScreenshot")
        self.safe_click(self.Area, "AreaDownScreenshot")

    # set desired category from the dropdown
    def set_category(self):
        self.safe_click(self.CategoryDropDown, "CategoryDropDownScreenshot")
        self.safe_click(self.Category, "CategoryScreenshot")

    def search(self):
        self.safe_click(self.Search, "SearchScreenshot")
