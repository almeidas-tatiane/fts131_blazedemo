import os
import time
from datetime import datetime

from selenium import webdriver  # Referencia ao Selenium WebDriver
import pytest  # Referencia ao Framework de Testes Unitario
from PIL import Image  # Biblioteca de manipulação de imagens
from selenium.webdriver.common.by import By

caminho_print = '../prints/' + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'


def testar_blazedemo():
    # Criação da pasta para guardar os prints desta execução
    os.makedirs(caminho_print)


    # Definindo que controlará o Chrome
    driver = webdriver.Chrome(executable_path='../drivers/chrome/96/chromedriver.exe')

    driver.get("https://www.blazedemo.com")
    time.sleep(3)  # pausa de 3 segundos - precisa remover depois - "Alfinete"
    # usa o proprio Selenium para tirar o print e salvar no disco
    driver.get_screenshot_as_file(caminho_print + 'home.png')
    time.sleep(3)  # pausa de 3 segundos - precisa remover depois - "Alfinete"
    driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    time.sleep(10)
    driver.get_screenshot_as_file(caminho_print + 'voos.png')
    time.sleep(3)
