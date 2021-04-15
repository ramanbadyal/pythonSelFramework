from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    phones = By.XPATH, "//div[@class='card h-100']"
    checkoutButton = By.CSS_SELECTOR,"a[class*='btn-primary']"
    name = By.XPATH,"//h4[@class='media-heading']/a"
    finalButton = By.CSS_SELECTOR,"button[class*='btn-success']"

    def products(self):
        return self.driver.find_elements(*CheckoutPage.phones)

    def getCheckout(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def getName(self):
        return self.driver.find_element(*CheckoutPage.name)

    def getFinalButton(self):
        self.driver.find_element(*CheckoutPage.finalButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
    # this is my third change.



