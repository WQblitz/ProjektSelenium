from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# Konfiguracja webdrivera
# Otwarcie przeglądarki oraz sprawdzenie poprawności procesu
def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get('https://www.olx.pl')
    self.driver.implicitly_wait(5)
    sleep(1)
    rodo_accept = self.driver.find_element(By.XPATH,"//*[@id='onetrust-accept-btn-handler'")
    title = self.driver.title
    print(title)
def tearDown(self):
    pass
# # Jeśli uruchomiono ten plik
# if __name__ == "__main__":
# # Uruchom testy
#     unittest.main(verbosity=3)