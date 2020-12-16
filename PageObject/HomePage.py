from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search_box = (By.ID, "twotabsearchtextbox")
    search_item = (By.ID, "nav-search-submit-text")

    # driver = webdriver.Chrome()

    def homepage_search(self):
        return self.driver.find_element(*HomePage.search_box)

    def click_on_search(self):
        return self.driver.find_element(*HomePage.search_item)
