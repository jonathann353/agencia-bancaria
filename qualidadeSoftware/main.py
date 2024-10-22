from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Iniciar maximizado

# Iniciar o navegador com o ChromeDriver gerenciado pelo WebDriver Manager
driver = webdriver.Chrome()

try:
    # Abrir o site saucedemo.com
    driver.get("https://www.saucedemo.com/")

    # Localizar o campo de usuário e senha
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")

    # Preencher o usuário e senha
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")

    # Fazer login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Esperar carregar a página principal
    time.sleep(3)  # Aguarde alguns segundos para garantir que a página foi carregada

    # Coletar os nomes e preços dos produtos
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")

    for product in products:
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"Produto: {name} - Preço: {price}")

finally:
    # Fechar o navegador
    driver.quit()
