from seleniumpagefactory.Pagefactory import PageFactory


# This class holds all the functions for the
class HomeScreen(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    # locators for the webelements in the login
    locators = {
        'PriceDropDown': ('CSS', "#ember1053 > div > div.selected-name"),
        'AreaDropDown': ('CSS', "#ember1088 > div > div.selected-name"),
        'CategoryDropDown': ('CSS', "#ember1120 > div > div.selected-name"),
        'PriceRange': ('ID', "ember1077"),
        'Area': ('ID', "ember1111"),
        'Category': ('ID', "ember1172"),
        'Search': ('ID', "ember1199")

    }

    # pick a price from the price dropdown
    def set_price(self):
        self.priceDropDown.click_button()
        self.PriceRange.click_button()

    # pick an area from the area dropdown
    def set_area(self):
        self.AreaDropDown.click_button()
        self.Area.click_button()

    #  pick a category from the category dropdown
    def set_category(self):
        self.CategoryDropDown.click_button()
        self.Category.click_button()

    # click the search button
    def search(self):
        self.Search.click_button()
