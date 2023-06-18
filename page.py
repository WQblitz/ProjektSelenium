from locator import *
from element import BasePageElement

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def is_title_matches(self):
        return "x-kom.pl" in self.driver.title
    def is_cookies_there(self):
        element = self.driver.find_element(*MainPageLocators.COOKIES)
    def click_cookie_button(self):
        element = self.driver.find_element(*MainPageLocators.ACCEPT_BUTTON)
        element.click()

    def click_account_button(self):
        element = self.driver.find_element(*MainPageLocators.ACCOUNT_BUTTON)
        element.click()

class AccountPage(BasePage):
    def new_account_button(self):
        element = self.driver.find_element(*AccountPageLocators.NEW_ACCOUNT_BUTTON)
        element.click()
