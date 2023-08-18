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
        'Register': ('XPATH','//*[@id="ember965"]/div/div[1]/div[2]/div/div[3]/div[1]/span'),
        'Name':('XPATH','//*[@id="ember1796"]'),
        'EnterEmail': ('XPATH', '//*[@id="ember1803"]'),
        'EnterPassword': ('XPATH', '//*[@id="valPass"]'),
        'ValPassword': ('XPATH', '//*[@id="ember1817"]'),
        'AgreeToPolicy': ('XPATH', '//*[@id="ember1823"]/div/span[1]/svg/circle'),
        'EnterBuyMe': ('XPATH', '//*[@id="ember1827"]'),

    }

    # set email and password and logs in to the website
    # takes screenshots and adds them to the allure
    def enter_credentials(self):
        try:
            self.LoginLink.click_button() # clicks the enter/register button
        except :
            allure.attach(self.driver.get_screenshot_as_png(), name="LoginLinkScreenshot", attachment_type=AttachmentType.PNG)
        try:
            self.Register.click_button() # clicks the register button
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="RegisterScreenshot",
                          attachment_type=AttachmentType.PNG)
        try:
            self.Name.set_text("tester") # enters a name
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="NameScreenshot", attachment_type=AttachmentType.PNG)

        try:
            self.EnterEmail.set_text("wodocir727@weishu8.com") # enters an email
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="EnterEmailScreenshot", attachment_type=AttachmentType.PNG)
        try:
            self.EnterPassword.set_text("Tester123") # enters a password
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="EnterPasswordScreenshot", attachment_type=AttachmentType.PNG)
        try:
            self.ValPassword.set_text("Tester123") # validate the password
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="ValPasswordScreenshot", attachment_type=AttachmentType.PNG)
        try:
            self.AgreeToPolicy.click_button() # agrees to site policy
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="AgreeToPolicyScreenshot", attachment_type=AttachmentType.PNG)
        try:
            self.EnterBuyMe.click_button() # register to the website
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="EnterBuyMeScreenshot", attachment_type=AttachmentType.PNG)

