from selenium.webdriver.common.by import By

class MainPageLocators(object):
    COOKIES = (By.XPATH, "//div[@role='dialog']")
    ACCEPT_BUTTON = (By.XPATH, '//button[@class="sc-15ih3hi-0 sc-1p1bjrl-9 dRLEBj"]')

class AccountPageLocators(object):
    MY_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/konto']//div[@class='sc-fz2r3r-1 fXBMII']//span[@class='sc-1tblmgq-0 sc-1tblmgq-4 SBMEx sc-fz2r3r-2 cDltcV']//*[name()='svg']")
    NOT_LOGGED_IN = (By.XPATH, "//h1[normalize-space()='Nie masz konta?']")
    NEW_ACCOUNT_BUTTON = (By.XPATH,"//a[contains(text(),'Załóż konto')]")
    NAME_INPUT = (By.XPATH,"//input[@placeholder='Imię (wymagane)']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='Nazwisko (wymagane)']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='E-mail (wymagane)']")
    SHORT_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Hasło (wymagane)']")
    SHORT_PASSWORD_ERROR = (By.XPATH, "//span[@class='sc-1nwq0d4-1 eCBqVz sc-qxbeow-0 gGHaGt']")
    REGISTER_ACCOUNT_BUTTON = (By.XPATH, "//span[@class='sc-6i4pc6-2 gIXjlD']")




