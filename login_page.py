from seleniumpagefactory.Pagefactory import PageFactory


class Login_Page(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'loginlink': ('XPATH', "//a[@aria-label='כניסה / הרשמה'][@role='link']"),
        'enteremail': ('ID', 'ember2079'),
        'enterpassword': ('ID', "ember2086"),
        'enterbuyme': ('ID', "ember2095"),

    }

    def enter_credentials(self):
        self.loginlink.click_button()
        self.enteremail.set_text("wodocir726@weishu8.com")
        self.enterpassword.set_text("Zubur123")
        self.enterbuyme.click_button()