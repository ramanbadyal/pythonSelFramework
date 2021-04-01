from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    editBox = By.XPATH, "//input[@id='country']"
    country = By.LINK_TEXT, "India"
    checkBox = By.XPATH, "//label[@for='checkbox2']"
    finalConfirm = By.XPATH,"//input[@type='submit']"
    finalCheck = By.CSS_SELECTOR,"div[class*='alert-success']"

    def getEditBox(self):
        return self.driver.find_element(*ConfirmPage.editBox)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getFinalConfirm(self):
        return self.driver.find_element(*ConfirmPage.finalConfirm)

    def getFinalText(self):
        return self.driver.find_element(*ConfirmPage.finalCheck)
