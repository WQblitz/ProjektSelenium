# Import niezbędnych modułów
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Stwórz instancję klasy Chrome()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://merito.pl/")

rodo = driver.find_element(By.CLASS_NAME, "eu-cookie-compliance-default-button")
rodo.click()
sleep(1)
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Poznaj WSB Merito")
element.click()

sleep(3)
driver.quit()