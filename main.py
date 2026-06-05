from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rhose.saude.pe.gov.br/Rhose/login.jsp")

time.sleep(2)

# campo login
usuario = driver.find_element(By.ID, "login")
usuario.send_keys("71052407412")

# campo senha
senha = driver.find_element(By.ID, "senha")
senha.send_keys("THI4G0v13")

# botão acessar
botao = driver.find_element(By.XPATH, "//button[contains(text(),'Acessar')]")
botao.click()

input("pressiona algo pra fechar")