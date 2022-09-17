import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



class TestActivationStep1(unittest.TestCase):

 #se executa ininte de fiecare test
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://beta.2nd.md/activate/step1')

    # se executa dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    # Test 1- daca url e corect
    def test_url1(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://beta.2nd.md/activate/step1'
        self.assertEqual(expected_url, actual_url, 'URL is incorrect')

   # Test 2- daca titlul e corect
    def test_title_page(self):
        actual_title = self.chrome.title
        expected_title = 'Activate Your Membership'
        self.assertTrue(expected_title in actual_title, 'Title is incorrect!')

   # Test4: Verificati ca butonul de login este displayed
    def test_displayed_btn(self):
        actual_btn = self.chrome.find_element(By.XPATH, '//*[@id="nextStep"]')
        self.assertTrue(actual_btn.is_displayed(), 'Button is not visible!')

    # Test5: Verificati ca atributul href al linkului ‘Elemental Selenium’ e corect
    def test_correct_atribute_element(self):
        actual = self.chrome.find_element(By.XPATH, '//*[contains(text(), "Sign")]').get_attribute('href')
        expected = "https://beta.2nd.md/login"
        self.assertEqual(actual, expected, '"Sign In" href attribute is incorrect')


    def test_validation_first_name(self):
        actual = self.chrome.find_element(By.XPATH, '//*[@id="nextStep"]')
        actual.click()
        sleep(1)

        actual_first_name = self.chrome.find_element(By.XPATH, '//*[@id="invalidFirstName"]').get_attribute('href')
        expected = 'wrong'
        self.assertEqual(actual_first_name, expected, 'Error msg not displayed')

    def test_validation_last_name(self):
        actual = self.chrome.find_element(By.XPATH, '//*[@id="nextStep"]').click()
        sleep(1)

        actual_last_name = self.chrome.find_element(By.XPATH, '//*[@id="invalidLastName"]').get_attribute('href')
        expected_attribute = 'wrong'
        self.assertEqual( actual_last_name, expected_attribute, 'Error msg not displayed')

    def test_activation(self):
        self.chrome.find_element(By.XPATH, '//*[@id="first"]').send_keys('Roxana')
        self.chrome.find_element(By.XPATH, '//*[@id="last"]').send_keys('Cucura')
        sleep(3)
