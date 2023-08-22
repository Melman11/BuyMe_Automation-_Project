from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
import allure
from allure_commons.types import AttachmentType


# This class holds all the functions for the
class SenderReceiver(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    # locators for the webelements in the sender and receiver info screen
    locators = {
        'ReceiverName': ('XPATH', '//*[@id="ember2769"]'),
        'EventDropDown': ('XPATH', '//*[@id="ember2774"]/div/div[1]/span'),
        'DesiredEvent': ('XPATH', '//*[@id="ember2797"]'),
        'CleanAll': ('XPATH', '//*[@id="ember1483"]/span[2]'),
        'TextBox': ('XPATH', '//*[@id="ember1483"]/textarea'),
        'UploadPicture': ('XPATH', '//*[@id="ember1491"]'),
        'ContinueButton': ('XPATH', '//*[@id="ember1493"]'),
        'ChooseEmail': ('XPATH', '//*[@id="ember2248"]/div[2]'),
        'ReceiverEmail': ('XPATH', '//*[@id="email"]'),
        'SenderName': ('XPATH', '//*[@id="ember2268"]'),
        'ContinueToPayment': ('XPATH', '//*[@id="ember2273"]')

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

    def gift_receiver(self):
        self.safe_set_text(self.ReceiverName, "John", "ReceiverNameScreenshot")  # set gift receiver name
        self.safe_click(self.EventDropDown, "EventDropDownScreenshot")  # clicks on the events dropdown
        self.safe_click(self.DesiredEvent, "DesiredEventScreenshot")  # choose desired event
        self.safe_click(self.CleanAll, "CleanAllScreenshot")  # cleans the textbox
        self.safe_set_text(self.TextBox,
                           "Happy Birthday, John! On this special day, may the sun shine a little brighter and the "
                           "stars twinkle with extra delight just for you. May your journey be filled with endless "
                           "laughter, boundless joy, and remarkable adventures that paint the canvas of your life "
                           "with vibrant and unforgettable colors.", "TextBoxScreenshot")  # writes the text

    # uploads the picture using send keys
    def upload_picture(self):
        try:
            file_location = "C:\\Users\\nivis\\Pictures\\Saved Pictures\\download.jfif"
            self.UploadPicture.send_keys(file_location)
            self.ContinueButton.click_button()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="UploadPictureScreenshot",
                          attachment_type=AttachmentType.PNG)

    # enters receivers email and sender name
    def enter_email(self):
        self.safe_click(self.ChooseEmail, "ChooseEmailScreenshot")  # Chose to use email
        self.safe_set_text(self.ReceiverEmail, "wodocir787@weishu8.com", "ReceiverEmailScreenshot")  # enters email
        self.SenderName.clear_text()  # clears textbox
        self.safe_set_text(self.SenderName, "Niv", "SenderNameScreenshot")  # enters sender name
        self.safe_click(self.ContinueToPayment, "ContinueToPaymentScreenshot")  # proceed to payment
