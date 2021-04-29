from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkoutPage import CheckoutPage
from pageObjects.confirmPage import ConfirmPage
from pageObjects.homePage import HomePage

from utilities.baseClass import baseClass


class TestOne(baseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)
        checkoutPage = homepage.shop()

        products = checkoutPage.products()

        for product in products:
            productName = product.find_element_by_xpath("div/h4").text
            if productName == "iphone X":
                product.find_element_by_xpath("div[2]/button").click()

        checkoutPage.getCheckout().click()

        actualName = checkoutPage.getName().text

        assert "iphone X" == actualName

        confirmPage = checkoutPage.getFinalButton()

        confirmPage.getEditBox().send_keys("ind")

        self.verifyLink("India")

        confirmPage.getCountry().click()

        confirmPage.getCheckBox().click()

        confirmPage.getFinalConfirm().click()

        finalText = confirmPage.getFinalText().text

        assert "Success! Thank you!" in finalText

        self.driver.get_screenshot_as_file("finalShot.png")

        #test1
