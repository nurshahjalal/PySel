from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver


    buy_it_again_text = (By.XPATH, "//span[contains(text(), 'Buy it again')]")
    allProductsDetails = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
    singleProduct = (By.CSS_SELECTOR, "[class='a-link-normal a-text-normal']")
    productPrice = (By.CSS_SELECTOR, "span[class='a-price']")

    def get_all_products_details(self):
        return self.driver.find_elements(*ProductPage.allProductsDetails)




