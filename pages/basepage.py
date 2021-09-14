from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser=browser
        self.url=url
        self.browser.implicitly_wait(timeout)
    def open_page(self):
        self.browser.get(self.url)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    def authorize_user(self, username, password):
        self.username=username
        self.password=password
        self.browser.find_element(*BasePageLocators.ENTER_BUTTON).click()
        self.browser.find_element(*BasePageLocators.LOGIN_FIELD).send_keys(self.username)
        self.browser.find_element(*BasePageLocators.LOGIN_ENTER_BUTTON).click()
        self.browser.find_element(*BasePageLocators.PASSWORD_FIELD).send_keys(self.password)
        self.browser.find_element(*BasePageLocators.LOGIN_ENTER_BUTTON).click()

    def should_be_password_field(self):
        assert self.is_element_present(*BasePageLocators.PASSWORD_FIELD)








