from seleniumpagefactory.Pagefactory import PageFactory


# This class holds all the functions for the login page
class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    # locators for the webelements in the login page
    locators = {
        'loginlink': ('XPATH', "//a[@aria-label='כניסה / הרשמה'][@role='link']"),
        'enteremail': ('ID', 'ember1888'),
        'enterpassword': ('ID', "ember1895"),
        'enterbuyme': ('ID', "ember1904"),

    }

    # Set email and password and logs in to the website
    def enter_credentials(self):
        self.loginlink.click_button()
        self.enteremail.set_text("wodocir726@weishu8.com")
        self.enterpassword.set_text("Zubur123")
        self.enterbuyme.click_button()
