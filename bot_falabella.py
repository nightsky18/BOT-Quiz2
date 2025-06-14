from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
import csv

# Configuración del driver
service = Service("driver/chromedriver.exe")
options= Options()
options.add_argument("--log-level=3")  # Reduce el nivel de log para evitar mensajes innecesarios
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Desactiva los logs de Chrome
options.add_argument("--disable-extensions")  # Desactiva las extensiones
# Abrir página
bot = webdriver.Chrome(service=service, options=options)
bot.get("https://www.falabella.com.co/falabella-co")
time.sleep(2) # Esperar a que la página cargue
bot.maximize_window()


# Buscar "Auriculares inalámbricos"
input = "Auriculares inalámbricos"
busqueda = bot.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[3]/div/div/input")
time.sleep(2)  # Esperar a que el elemento esté disponible 
busqueda.click()
busqueda.send_keys(input)
busqueda.send_keys(Keys.ENTER)
time.sleep(2)  # Esperar a que la página cargue

#ubicarse en filtros

marca = bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div[2]/div/ul/li[3]/button")
bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Desplazarse hacia abajo para cargar más filtros
time.sleep(2)  # Esperar a que el elemento esté disponible
marca.click()
time.sleep(2)  # Esperar a que la página cargue

# Seleccionar marca "XIAOMI"
marca_xiaomi = bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div[2]/div/ul/li[3]/div/ul/li[1]/label/input")
time.sleep(2)
marca_xiaomi.click()
time.sleep(5)  # Esperar a que la página cargue


marca = bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div[2]/div/ul/li[3]/button")
bot.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
marca.click()
# Seleccionar marca "LENOVO"
marca_lenovo = bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div[3]/div/ul/li[2]/div/ul/li[2]/label/input")
time.sleep(2)
marca_lenovo.click()
time.sleep(5)  # Esperar a que la página cargue

                                               


bot.quit()  # Cerrar el navegador


