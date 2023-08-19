from seleniumpagefactory.Pagefactory import PageFactory
import allure
from allure_commons.types import AttachmentType


# This class holds all the functions for the
class PickBusiness(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    # locators for the webelements in the login page
    locators = {
        "SelectedBusiness": ('XPATH', '//*[@id="ember1736"]'),
        "EnterAmount": ('XPATH', '//*[@id="ember1895"]'),
        "ConfirmAmount": ('XPATH', '//*[@id="ember1901"]')
    }

    # this function adds an allure report screenshot as an exception for every click_button() command
    def safe_click(self, element, screenshot_name):
        try:
            element.click_button()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=AttachmentType.PNG)

    # this function adds an allure report screenshot as an exception for every set_text() command
    def safe_set_text(self, element, text, screenshot_name):
        try:
            element.set_text(text)
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=AttachmentType.PNG)

    # picks a business
    def select_business(self):
        self.safe_click(self.SelectedBusiness, "SelectedBusinessScreenshot")

    # set desire amount of money and confirms
    def enter_amount(self):
        self.safe_click(self.EnterAmount, "EnterAmountClickScreenshot")
        self.safe_set_text(self.EnterAmount, '200', "EnterAmountSetScreenshot")
        self.safe_click(self.ConfirmAmount, "ConfirmAmountScreenshot")
