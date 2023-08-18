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

    # pick a price from the price dropdown
    def set_price(self):
        try:
            self.priceDropDown.click_button()  # cliks on the dropdown for price range
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="PriceDropDownScreenshot",
                          attachment_type=AttachmentType.PNG)
        try:
            self.PriceRange.click_button()  # clicks on the desired price
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="PriceRangeScreenshot",
                          attachment_type=AttachmentType.PNG)

    # pick an area from the area dropdown
    def set_area(self):
        try:
            self.AreaDropDown.click_button()  # cliks on the dropdown for area
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="AreaDropDownScreenshot",
                          attachment_type=AttachmentType.PNG)
        try:
            self.Area.click_button()  # clicks on the desired area
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="AreaDownScreenshot",
                          attachment_type=AttachmentType.PNG)

    #  pick a category from the category dropdown
    def set_category(self):
        try:
            self.CategoryDropDown.click_button()  # cliks on the dropdown for category
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="CategoryDropDownScreenshot",
                          attachment_type=AttachmentType.PNG)
        try:
            self.Category.click_button()  # clicks on the desired category
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="CategoryScreenshot",
                          attachment_type=AttachmentType.PNG)

    # click the search button
    def search(self):
        try:
            self.Search.click_button()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="SearchScreenshot", attachment_type=AttachmentType.PNG)
