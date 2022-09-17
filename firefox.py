import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class Test_Firefox(unittest.TestCase):

    # se ruleaza inainte de fiecare test
    def setUp(self):
        self.firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.firefox.maximize_window()
        self.firefox.get('https://the-internet.herokuapp.com/login')

       # se ruleaza dupa fiecare test
    def tearDown(self):
        self.firefox.quit()

        # Test 1- daca url e corect
    def test_url(self):
        actual_url = self.firefox.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected_url, actual_url, 'The URL is incorrect')

        # Test 2- daca titlul e corect
    def test_page_tittle(self):
        actual_browser_title = self.firefox.title
        expected_browser_title = 'The Internet'
        self.assertEqual(actual_browser_title, expected_browser_title, 'The page title is not the correct one!')
        sleep(1)

        # Test 3-XPATH
    def test_xpath(self):
        actual_page_title = self.firefox.find_element(By.XPATH, '//h2[text()="Login Page"]').text
        expected_page_title = 'Login Page'
        self.assertEqual(actual_page_title, expected_page_title, 'The Page Title is incorrect!')
        print(page_title)
        sleep(1)

        # Test 4- butonul de login este displayed
    def test_login_btn_visible(self):
        actual_login_btn_text = self.firefox.find_element(By.XPATH, '//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]').text
        expected_login_btn_text = 'Login'
        self.assertEqual(actual_login_btn_text, expected_login_btn_text, 'Button not visible')
        print(expected_login_btn_text)
        sleep(1)

        # Test 5- atributul href al linkului ‘Elemental Selenium’ e corect
    def test_correct_atribute_element(self):
        actual_attribute = self.firefox.find_element(By.XPATH, '//*[contains(text(), "Elemental")]').get_attribute('href')
        expected_link_attribute = "http://elementalselenium.com/"
        self.assertEqual(actual_attribute, expected_link_attribute, 'Attribute is incorrect')
        sleep(1)

        # Test 6- eroarea displayed
    def test_displayed_error(self):
        username = self.firefox.find_element(By.XPATH, '//*[@id="username"]')
        username.send_keys('wrong')
        password = self.firefox.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('wrong')
        login_btn = self.firefox.find_element(By.XPATH,'//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]')
        login_btn.click()
        sleep(5)
        error_msg = self.firefox.find_element(By.XPATH, '//*[@class="flash error"]').text
        print(error_msg)
        expected_error_msg = 'Your username is invalid'
        self.assertTrue(expected_error_msg in error_msg, 'Error message is not the expected one!')
        sleep(1)

        # Test 7- flash error
    def test_flash_error(self):
        username = self.firefox.find_element(By.XPATH, '//*[@id="username"]')
        username.send_keys('')
        password = self.firefox.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('')
        login_btn = self.firefox.find_element(By.XPATH,'//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]')
        login_btn.click()
        close_error_msg = self.firefox.find_element(By.XPATH, '//a[@class="close"]')
        close_error_msg.click()
        sleep(5)
        show_error_message = self.firefox.find_elements(By.XPATH, '//*[@class="flash error"]')
        self.assertEqual(len(show_error_message), 0, 'No flash error found')
        print(len(show_error_message))
        #self.assertEqual(len(error_messages) == 0, 'No flash error found !')
        sleep(1)

        # Test 8- mesaj de eroare corect
    def test_invalid_credentiales_error(self):
        actual_label_elements = self.firefox.find_elements(By.XPATH, '//label')
        expected_label_user = "Username"
        expected_label_psw = "Password"
        self.assertEqual(actual_label_elements[0].text, expected_label_user, "The 'Username' Label/text is NOT the correct one")
        self.assertEqual(actual_label_elements[1].text, expected_label_psw, "The 'Password' Label/text is NOT the correct one")
        sleep(2)

    # Test 9- credentialele corecte
    def test_valid_login(self):
        username = self.firefox.find_element(By.XPATH, '//*[@id="username"]')
        username.send_keys('tomsmith')
        password = self.firefox.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('SuperSecretPassword!')
        login_btn = self.firefox.find_element(By.XPATH,'//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]')
        login_btn.click()
        sleep(2)

        actual_url = self.firefox.current_url
        expected_url = "https://the-internet.herokuapp.com/secure"
        self.assertEqual(actual_url, expected_url)
        expected_URL2 = 'secure area'
        self.assertTrue(expected_url in actual_url,'Text message text is incorrect' )
        sleep(2)

    # Test 10- login cu credentiale corecte
    def test_valid_login2(self):
        self.firefox.find_element(By.XPATH, '//*[@id="username"]').send_keys('tomsmith')
        self.firefox.find_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
        self.firefox.find_element(By.XPATH,'//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]').click()
        self.firefox.find_element(By.XPATH, '//*[@class="icon-2x icon-signout"]').click()

        actual_url = self.firefox.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        self.assertEqual(actual_url, expected_url, 'URL is incorrect!')
