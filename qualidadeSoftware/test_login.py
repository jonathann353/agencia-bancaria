import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class SauceDemoLoginTest(unittest.TestCase):

    def setUp(self):
        """Configurações antes de cada teste"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
    
    def test_login_success(self):
        """Teste de login com credenciais válidas"""
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Verifica se o login foi bem-sucedido ao verificar a presença do título 'Products'
        products_title = driver.find_element(By.CLASS_NAME, "title").text
        self.assertEqual(products_title, "Products")

    def test_login_failure_invalid_credentials(self):
        """Teste de login com credenciais inválidas"""
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("invalid_user")
        driver.find_element(By.ID, "password").send_keys("invalid_password")
        driver.find_element(By.ID, "login-button").click()
        
        # Verifica se a mensagem de erro está presente
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Username and password do not match", error_message)

    def test_login_failure_empty_username(self):
        """Teste de login com campo de nome de usuário vazio"""
        driver = self.driver
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Verifica se a mensagem de erro aparece por causa do nome de usuário vazio
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Username is required", error_message)

    def test_login_failure_empty_password(self):
        """Teste de login com campo de senha vazio"""
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "login-button").click()

        # Verifica se a mensagem de erro aparece por causa da senha vazia
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Password is required", error_message)

    def tearDown(self):
        """Finaliza o navegador após cada teste"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
