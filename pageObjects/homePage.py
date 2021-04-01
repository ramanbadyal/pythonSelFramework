from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    shopButton = (By.CSS_SELECTOR, "a[href*='shop']")

    def shop(self):
      self.driver.find_element(*HomePage.shopButton).click()
      checkoutPage = CheckoutPage(self.driver)
      return checkoutPage
