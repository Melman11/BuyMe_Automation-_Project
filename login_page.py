from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
import allure
from allure_commons.types import AttachmentType


# This class holds all the functions for the login page
class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    # locators for the webelements in the login page
    locators = {
        'LoginLink': ('XPATH', '//*[@id="ember1005"]/div/ul[1]/li[3]/a'),
        'Register': ('XPATH', '//*[@id="ember981"]/div/div[1]/div[2]/div/div[3]/div[1]/span'),
        'Name': ('XPATH', '//*[@id="ember1796"]'),
        'EnterEmail': ('XPATH', '//*[@id="ember1803"]'),
        'EnterPassword': ('XPATH', '//*[@id="valPass"]'),
        'ValPassword': ('XPATH', '//*[@id="ember1817"]'),
        'AgreeToPolicy': ('XPATH', '//*[@id="ember1823"]/div/span[1]/svg/circle'),
        'EnterBuyMe': ('XPATH', '//*[@id="ember1827"]'),

    }

    # this function adds an allure report screenshot as an exception for every click_button() command + explicit wait
    def safe_click(self, element, screenshot_name):
        try:
            wait = WebDriverWait(self.driver, 13)
            clickable_element = wait.until(EC.element_to_be_clickable((By.ID, element.id)))
            clickable_element.click_button()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=AttachmentType.PNG)

    # this function adds an allure report screenshot as an exception for every set_text() command + explicit wait
    def safe_set_text(self, element, text, screenshot_name):
        try:
            wait = WebDriverWait(self.driver, 13)
            visible_element = wait.until(EC.visibility_of_element_located((By.ID, element.id)))
            visible_element.clear()
            visible_element.set_text(text)
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=AttachmentType.PNG)

    def enter_credentials(self):
        self.safe_click(self.LoginLink, "LoginLinkScreenshot")  # clicks the login link
        self.safe_click(self.Register, "RegisterScreenshot")  # clicks the register button
        self.safe_set_text(self.Name, "tester", "NameScreenshot")  # enters name
        self.safe_set_text(self.EnterEmail, "wodocir727@weishu8.com", "EnterEmailScreenshot")  # enters email
        self.safe_set_text(self.EnterPassword, "Tester123", "EnterPasswordScreenshot")  # enters password
        self.safe_set_text(self.ValPassword, "Tester123", "ValPasswordScreenshot")  # validates password
        self.safe_click(self.AgreeToPolicy, "AgreeToPolicyScreenshot")  # agrees to site policy
        self.safe_click(self.EnterBuyMe, "EnterBuyMeScreenshot")  # enters the site
