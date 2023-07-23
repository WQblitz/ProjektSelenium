from selenium import webdriver
from locator import *
from selenium.webdriver.common.keys import Keys
from element import BasePageElement


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def is_title_matches_mainPage(self):
        return "x-kom.pl" in self.driver.title
    def is_cookies_there(self):
        element = self.driver.find_element(*MainPageLocators.COOKIES)
    def click_cookie_button(self):
        element = self.driver.find_element(*MainPageLocators.ACCEPT_BUTTON)
        element.click()
    def search_product(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH)
        element.send_keys("Dysk HDD 4TB", Keys.ENTER)

    def search_product_2(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH)
        element.send_keys("Dysk HDD 24TB", Keys.ENTER)

class AccountPage(BasePage):
    def no_account_logged(self):
        element = self.driver.find_element(*AccountPageLocators.NOT_LOGGED_IN)
    def my_account_button(self):
        element = self.driver.find_element(*AccountPageLocators.MY_ACCOUNT_BUTTON)
        element.click()
    def new_account_button(self):
        element = self.driver.find_element(*AccountPageLocators.NEW_ACCOUNT_BUTTON)
        element.click()
    def is_title_matches_RegisterPage(self):
        return "Rejestracja" in self.driver.title

    def input_name(self):
        element = self.driver.find_element(*AccountPageLocators.NAME_INPUT)
        element.send_keys(self.fakeData.first_name())
    def input_lastname(self):
        element = self.driver.find_element(*AccountPageLocators.LASTNAME_INPUT)
        element.send_keys(self.fakeData.last_name())
    def input_email(self):
        element = self.driver.find_element(*AccountPageLocators.EMAIL_INPUT)
        element.send_keys(self.fakeData.email())
    def input_password_tooShort(self):
        element = self.driver.find_element(*AccountPageLocators.SHORT_PASSWORD_INPUT)
        element.send_keys(self.fakeData.password(7, False, False, False, True))
    def input_password_correct(self):
        element = self.driver.find_element(*AccountPageLocators.SHORT_PASSWORD_INPUT)
        element.clear()
        element.send_keys(self.fakeData.password(8, False, False, False, True))
    def short_password_error(self):
        element = self.driver.find_element(*AccountPageLocators.SHORT_PASSWORD_ERROR)
    def register_accoount_button(self):
        element = self.driver.find_element(*AccountPageLocators.REGISTER_ACCOUNT_BUTTON)
    def accept_rules_checkbox(self):
        element = self.driver.find_element(*AccountPageLocators.RULES_CHECKBOX).click()
