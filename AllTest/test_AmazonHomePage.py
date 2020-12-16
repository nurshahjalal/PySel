from selenium.webdriver.common.by import By
from BaseTest.TestBase import TestBase
from PageObject.HomePage import HomePage
from PageObject.ProductPage import ProductPage


class TestHomePage(TestBase):

    def test_homepage(self):
        driver = HomePage(self.driver)
        logger = self.get_logger()
        driver.homepage_search().send_keys("carp")
        logger.info(" Step 1: Enter Carp in the search box")

        driver.click_on_search().click()
        logger.info(" Step 2: click on search")

    def test_count_all_products_prices(self):
        driver = ProductPage(self.driver)
        logger = self.get_logger()
        productDetails = driver.get_all_products_details()
        for prod in productDetails:
            try:
                product = prod.find_element(*driver.singleProduct)
                price = prod.find_element(*driver.productPrice)
                fullprice = ".".join(price.text.split("\n"))
                logger.info(f"{product.text}\n {fullprice}")

            except:
                logger.info("Product details not found")




