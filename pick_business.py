from seleniumpagefactory.Pagefactory import PageFactory


# This class holds all the functions for the
class PickBusiness(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    # locators for the webelements in the login page
    locators = {
        "SelectedBusiness": ('CSS', "#ember2160"),
        "EnterAmount": ('ID', "ember2318"),
        "ConfirmAmount": ('ID', "ember2324")

    }

    # clicks on the selected business
    def select_business(self):
        self.SelectedBusiness.click_button()

    # enters and confirms the amount of money
    def enter_amount(self):
        self.EnterAmount.click_button()
        self.EnterAmount.set_text('200')
        self.ConfirmAmount.click_button()
