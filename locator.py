from selenium.webdriver.common.by import By

class MainPageLocators(object):
    COOKIES = (By.XPATH, "//a[normalize-space()='ciasteczek']")
    ACCEPT_BUTTON = (By.XPATH, '//button[@class="sc-15ih3hi-0 sc-1p1bjrl-9 dRLEBj"]')
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/konto']//div[@class='sc-fz2r3r-1 fXBMII']//span[@class='sc-1tblmgq-0 sc-1tblmgq-4 SBMEx sc-fz2r3r-2 cDltcV']//*[name()='svg']")

class AccountPageLocators(object):
    NEW_ACCOUNT_BUTTON = (By.XPATH,"//a[contains(text(),'Załóż konto')]")

