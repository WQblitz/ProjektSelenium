import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from faker import Faker


# DANE TESTOWE


class PierwszyTest(unittest.TestCase):
    def setUp(self):
        # Warunki wstępne:
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.eobuwie.com.pl/")
        self.driver.implicitly_wait(10)
        cookie_accept = self.driver.find_element(By.XPATH, '//div[@class="e-consents-alert__actions"]/button[1]')
        cookie_accept.click()
        self.fake = Faker("pl_PL")

        # oczekiwanie na rezultaty:
        sleep(4)

    def testNoNameEntered(self):
        # 1. Kliknij „Zarejestruj”
        register_a = self.driver.find_element(By.XPATH, '//a[@data-testid="header-register-link"]').click()
        self.driver.implicitly_wait(10)
        # 2. Wpisz nazwisko
        lastname_input = self.driver.find_element(By.ID, "lastname")
        lastname_input.send_keys(self.fake.last_name())
        self.driver.implicitly_wait(10)
        # 3. Wpisz adres e-mail
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys(self.fake.email())
        self.driver.implicitly_wait(10)
        # 4. Wpisz haslo
        password = self.fake.password()
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        self.driver.implicitly_wait(10)
        # 5. Wpisz potwierdzenie hasla
        password_input = self.driver.find_element(By.NAME, "confirmation")
        password_input.send_keys(password)
        self.driver.implicitly_wait(10)
        # 6. Zaznaczenie oswiadczenia zapoznania sie z regulaminem
        checkbox_statement = self.driver.find_element(By.XPATH, '//label[@class="checkbox-wrapper__label"]').click()
        # 7. Kliknij rejestruj
        create_account = self.driver.find_element(By.ID, "create-account").click()

        sleep(5)
        # OCZEKIWANY REZULTAT:
        # 1. Uzytkownik otrzymuje informacje "To pole jest wymagane" pod polem wprowadzenia imienia
        # 1.1 Szukanie wszystkich komunikatow o bledzie uzytkownika
        user_error_messages = self.driver.find_elements(By.XPATH, '//span[@class="form-error"]')
        # 1.2 Sprawdzenie czy liczba komunikatow o bledzie wynosi 1
        self.assertEqual(1, len(user_error_messages))
        # 1.3 Sprawdzenie czy tresc komunikatu jest widoczna i brzmi "To pole jest wymagane"
        self.assertEqual("To pole jest wymagane", user_error_messages[0].text)
        # 1.4 Sprawdzenie lokalizacji komunikatu (czy dotyczy pola Imie?)
        error_message = self.driver.find_element(
            locate_with(By.XPATH, '//span[@class="form-error"]').near({By.ID: "lastname"}))
        # 1.5 Sprawdzenie czy element odszukany obiema metodami to ten sam element
        self.assertEqual(user_error_messages[0].id, error_message.id)

        # oczekiwanie na rezultaty:
        sleep(2)

    def tearDown(self):
        pass


# Jeśli uruchomiono ten plik
if __name__ == "__main__":
    # Uruchom testy
    unittest.main(verbosity=0)

