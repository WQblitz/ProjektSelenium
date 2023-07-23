#  PROJEKT AUTOMATYZACJI TESTÓW WITRYNY X-KOM.PL PRZY WYKORZYSTANIU PROGRAMOWANIA
#  OBIEKTOWEGO PYTHON ORAZ NARZĘDZIA SELENIUM WRAZ Z UNITTEST

#  Projekt wykorzystuje wirtualne środowisko (venv) - lista zainstalowanych modułów jest dostępna w dokumentacji.
#  W projekcie "ProjektSelenium" powinny znajdować się cztery pliki:
#  main.py
#  locator.py
#  page.py

#  Implementacja niezbędnych modułów:
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException



#  Import danych zawartych w pliku page.py
import page

#  Import modułów zbędnych w działaniu testów:

#  Moduł pozwalający na wyświetlenie aktualnej daty
from datetime import datetime

#  Moduł generujący różne dane takie jak imiona, nazwiska, adresy etc.:
from faker import Faker

#  DANE TESTOWE
#  Stworzenie klasy dla pierwszego przypadku testowego wraz z konfiguracją

#  Wygenerowanie tekstu dla łatwiejszego zobrazowania rezultatu końcowego testu
print("PROJEKT SELENIUM+UNITTEST")
now = datetime.now()
nowTime = now.strftime("%d/%m/%Y %H:%M:%S")
print("Testy uruchomiono: ", nowTime)
print("Rezultaty testów:")


class TestXKom(unittest.TestCase):

#  Określenie warunków wstępnych:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.x-kom.pl/")
        self.fakeData = Faker("pl_PL")

#  Pierwszy test sprawdzający czy otwarta strona to faktycznie strona o odpowiednim tytule
    def test_a_main_page_title(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_mainPage()
        if main_page.is_title_matches_mainPage():
            print("Załadowano poprawną stronę główną")
        else:
            print("Załadowano złą stronę")
#  Kolejny test sprawdzający czy po pierwszym wejściu na stronę pojawia się komunikat o ciasteczkach oraz czy działa akceptacja komunikatu

    def test_b_cookie_accept(self):
        try:
            cookies = page.MainPage.is_cookies_there(self)
            print("Znaleziono komunikat dot. ciasteczek")
        except NoSuchElementException:
            print("Nie znaleziono komunikatu dot. ciasteczek")
        assert True
        page.MainPage(self.driver).click_cookie_button()

#  Kolejny test, w którym będzie sprawdzana funkcja zakładania konta
#  Funkcja implicitly_wait() jest miejscami wymagana, ze względu na to, że niektóre fragmenty kodu mogą być wykonywane jeszcze zanim konkretny element strony będzie widoczny
#  co będzie skutkowało błędami. Na niektórych etapach wykorzystano funkcję sleep(), która wymusza zatrzymanie wykonywania instrukcji na określony czas.
    def test_c_account_creation_page(self):

        page.MainPage(self.driver).click_cookie_button()
        accountPage = page.AccountPage(self.driver)
        sleep(3)
        page.AccountPage(self.driver).my_account_button()
        sleep(2)
        try:
            no_account = page.AccountPage.no_account_logged(self)
            print("Załadowano poprawną stronę: Moje konto")
        except NoSuchElementException:
            print("Nie znaleziono odnośnika do logowania lub rejestracji")
        assert True
        page.AccountPage(self.driver).new_account_button()
        sleep(3)
        assert accountPage.is_title_matches_RegisterPage() == True
        if accountPage.is_title_matches_RegisterPage() == True:
            print("Załadowano poprawną stronę: Rejestracja")
        else:
            print("Załadowano złą stronę")

    def test_d_create_account(self):
#  Rozpoczęcie testu bezpośrednio poprzez link do rejestracji - nie ma potrzeby dublowania powyższego testu, a przy okazji skracamy czas testu.
        self.driver.get("https://www.x-kom.pl/rejestracja")
        firstName_input = page.AccountPage.input_name(self)
        lastName_input = page.AccountPage.input_lastname(self)
        email_input = page.AccountPage.input_email(self)
        short_password_input = page.AccountPage.input_password_tooShort(self)
        sleep(3)
        rules_checkbox_click = page.AccountPage.accept_rules_checkbox(self)
        rules_checkbox_click2 = page.AccountPage.accept_rules_checkbox(self)
        sleep(2)
        if self.driver.find_element(By.XPATH, "//span[@class='sc-1nwq0d4-1 eCBqVz sc-qxbeow-0 gGHaGt']").is_displayed():
            print("Test wartości granicznej - hasło zbyt krótkie")
        else:
            print("Błąd - oczekiwany komunikat o zbyt krótkim haśle")
        sleep(3)
    @unittest.skip
    def test_e_create_account(self):
#  Rozpoczęcie testu bezpośrednio poprzez link do rejestracji - nie ma potrzeby dublowania powyższego testu, a przy okazji skracamy czas testu.
        self.driver.get("https://www.x-kom.pl/rejestracja")
        firstName_input = page.AccountPage.input_name(self)
        lastName_input = page.AccountPage.input_lastname(self)
        email_input = page.AccountPage.input_email(self)
        short_password_input = page.AccountPage.input_password_correct(self)
        sleep(3)
        rules_checkbox_click = page.AccountPage.accept_rules_checkbox(self)
        rules_checkbox_click2 = page.AccountPage.accept_rules_checkbox(self)
        sleep(2)
        if self.driver.find_element(By.XPATH, "//span[@class='sc-1nwq0d4-1 eCBqVz sc-qxbeow-0 gGHaGt']").is_displayed():
            print("Test wartości granicznej - hasło o odpowiedniej długości")
        else:
            print("Błąd - oczekiwany brak powiadomienia o zbyt krótkim haśle")
        sleep(3)
    pass

# Test działania wyszukiwarki produktów:
    def test_f_search_product(self):
        self.driver.get("https://www.x-kom.pl")
        sleep(3)
        page.MainPage(self.driver).click_cookie_button()
        search = page.MainPage.search_product(self)
        sleep(5)
        count = self.driver.find_elements(By.XPATH, "//h3[contains(@title,'4TB')]")
#  Należy zwrócić uwagę na ^^ liczbę mnogą funkcji find_elementS - dopiero wtedy otrzymamy listę znalezionych elementów, którą funkcja len() może zliczyć
        print("Znaleziono",len(count), "pasujących wyników z 30 wyświetlonych na stronie")

#  Test sprawdzający ilość wyświetlonych dysków 4TB podczas wyszukiwania znacznie większej ilości
    def test_g_search_product(self):
        self.driver.get("https://www.x-kom.pl")
        sleep(3)
        page.MainPage(self.driver).click_cookie_button()
        search = page.MainPage.search_product_2(self)
        sleep(5)
        count = len(self.driver.find_elements(By.XPATH, "//h3[contains(@title,' 4TB')]"))
        assert count != 0
        print("Test nieudany - nie znaleziono pasujących wyników")
#Funkcja tearDown wymagana jest do "zamknięcia" testu w momencie gdy UnitTest go zakończy.
#Funkcja ta pozwala na rozpoczęcie każdego kolejnego testu na świeżo - po zamknięciu poprzedniego
def tearDown(self):
        self.driver.close()


# Jeśli uruchomiono ten plik
if __name__ == "__main__":
    # Uruchom testy
    unittest.main()
