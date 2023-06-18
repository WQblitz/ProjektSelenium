#PROJEKT AUTOMATYZACJI TESTÓW WITRYNY X-KOM.PL PRZY WYKORZYSTANIU PROGRAMOWANIA
#OBIEKTOWEGO PYTHON ORAZ NARZĘDZIA SELENIUM WRAZ Z UNITTEST

#Projekt wykorzystuje wirtualne środowisko (venv) - lista zainstalowanych modułów jest dostępna w dokumentacji.
#W projekcie "ProjektSelenium" powinny znajdować się cztery pliki:
#main.py
#locator.py
#page.py

#Implementacja niezbędnych modułów:
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import NoSuchElementException


#Import modułów zbędnych - mają one tylko ułatwić "wymyślanie" danych, które będą wykorzystane
#w testach oraz urozmaicić wizualnie zwracane treści
from faker import Faker
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText("PROJEKT SELENIUM"))

#Import danych zawartych w pliku page.py
import page

# DANE TESTOWE
#Stworzenie klasy dla pierwszego przypadku testowego wraz z konfiguracją

class TestXKom(unittest.TestCase):
#Określenie warunków wstępnych:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.x-kom.pl/")
        self.fakeData = Faker("pl_PL")
#Funkcja sleep() nie jest niezbędna w tym kodzie, ma na celu tylko i wyłącznie sztucznie opóźnić wykonywanie poleceń przez interpreter
#aby w móc podejrzeć działanie webdrivera
    sleep(4)

#Pierwszy test sprawdzający czy otwarta strona to faktycznie strona o odpowiednim tytule
    def test_MainPageTitle(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        if mainPage.is_title_matches() == True:
            print("Załadowano poprawną stronę")
        else:
            print("Załadowano złą stronę")
#Pierwszy test sprawdzający czy po pierwszym wejściu na stronę pojawia się komunikat o ciasteczkach oraz czy działa akceptacja komunikatu

    def test_CookieAccept(self):
        try:
            cookies = page.MainPage.is_cookies_there(self)
            print("Znaleziono komunikat dot. ciasteczek!")
        except NoSuchElementException:
            print("Nie znaleziono komunikatu dot. ciasteczek")
        assert True






#     def testNoNameEntered(self):
#     # 1. Kliknij „Moje konto”
#         find_account = self.driver.find_element(By.XPATH, "//a[@href='/konto']//div[@class='sc-fz2r3r-1 fXBMII']//span[@class='sc-1tblmgq-0 sc-1tblmgq-4 SBMEx sc-fz2r3r-2 cDltcV']//*[name()='svg']").click()
#         sleep(2)
#         register = self.driver.find_element(By.XPATH, "//a[contains(text(),'Załóż konto')]").click()
#         self.driver.implicitly_wait(5)
#     # 2. Wpisz imię
#         firstName_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Imię (wymagane)']")
#         self.driver.implicitly_wait(5)
#         firstName_input.send_keys(self.fakeData.first_name())
#         self.driver.implicitly_wait(5)
#
#     # 3. Wpisz nazwisko
#         lastname_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Nazwisko (wymagane)']")
#         self.driver.implicitly_wait(5)
#         lastname_input.send_keys(self.fakeData.last_name())
#         self.driver.implicitly_wait(5)
#
#         # 3. Wpisz adres e-mail
#         email_input = self.driver.find_element(By.XPATH, "//input[@placeholder='E-mail (wymagane)']")
#         email_input.send_keys(self.fakeData.email())
#         self.driver.implicitly_wait(5)
#
#         # 4. Wpisz haslo
#         password = self.fakeData.password()
#         password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Hasło (wymagane)']")
#         password_input.send_keys(password)
#         self.driver.implicitly_wait(5)
#
#         # 6. Zaznaczenie zgody na wszystkie pozycje
#         checkboxStatement_all = self.driver.find_element(By.XPATH, "//div[@class='sc-4mwtey-0 cHXQmZ sc-ldtoi0-6 QTblv']//div[@class='sc-3qnozx-1 bhmstJ']").click()
#         # 7. Zaznaczenie zapoznania się z regulaminem
#         checkboxStatement_statue = self.driver.find_element(By.XPATH, "//div[@class='sc-ldtoi0-10 vFjnk']//div[1]//div[1]//label[1]//div[1]").click()
#         # 8. Zaznaczenie zgody na newslettera
#
#         checkboxStatement_newsletter = self.driver.find_element(By.XPATH, "//body/div[@id='app']/div[@class='sc-14ybyi4-0 iToDFs sc-3vw8wn-2 gCodMm']/div[@class='sc-1s1zksu-0 yuDxM sc-3vw8wn-4 eojLRM']/div[@class='sc-1s1zksu-0 sc-1s1zksu-1 hHQkLn']/div[@class='sc-1s1zksu-0 hstFlZ sc-raujvo-2 cfywri']/div[@class='sc-raujvo-1 ffgcjl']/form[@class='sc-qtqqzt-1 fYnsBZ']/div[@class='sc-qtqqzt-0 jNFeVc']/div[@class='sc-qtqqzt-8 gimKOM']/div[@class='sc-ldtoi0-0 dCgOsh sc-qtqqzt-5 kBTOEZ']/div[@class='sc-ldtoi0-10 vFjnk']/div[@class='sc-1jh87d2-1 jvxkzA sc-ldtoi0-11 dpDrXq']/div[2]/div[1]/label[1]/div[1]").click()
#         # 7. Kliknij rejestruj
#         # Ze względu na to, że wykorzystywana jest witryna na produkcji poprawne założenie testowego konta odbędzie się w późniejszym etapie
#         #create_account = self.driver.find_element(By.XPATH, "//span[@class='sc-6i4pc6-2 gIXjlD']".click()
#
#         sleep(5)
#         # OCZEKIWANY REZULTAT:
#         # 1. Uzytkownik otrzymuje informacje "To pole jest wymagane" pod polem wprowadzenia imienia
#         # 1.1 Szukanie wszystkich komunikatow o bledzie uzytkownika
#         user_error_messages = self.driver.find_elements(By.XPATH, '//span[@class="form-error"]')
#         # 1.2 Sprawdzenie czy liczba komunikatow o bledzie wynosi 1
#         self.assertEqual(1, len(user_error_messages))
#         # 1.3 Sprawdzenie czy tresc komunikatu jest widoczna i brzmi "To pole jest wymagane"
#         self.assertEqual("To pole jest wymagane", user_error_messages[0].text)
#         # 1.4 Sprawdzenie lokalizacji komunikatu (czy dotyczy pola Imie?)
#         error_message = self.driver.find_element(
#             locate_with(By.XPATH, '//span[@class="form-error"]').near({By.ID: "lastname"}))
#         # 1.5 Sprawdzenie czy element odszukany obiema metodami to ten sam element
#         self.assertEqual(user_error_messages[0].id, error_message.id)
#
# #Oczekiwanie na rezultaty:
#         sleep(2)

#Funkcja tearDown wymagana jest do "zamknięcia" testu w momencie gdy UnitTest go zakończy.
#Funkcja ta pozwala na rozpoczęcie każdego kolejnego testu na świeżo - po zamknięciu poprzedniego
    def tearDown(self):
        self.driver.close()


# Jeśli uruchomiono ten plik
if __name__ == "__main__":
    # Uruchom testy
    unittest.main()

