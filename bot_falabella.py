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

marca_btn = bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div[2]/div/ul/li[3]/button")
bot.execute_script("arguments[0].scrollIntoView();", marca_btn)
time.sleep(1)
marca_btn.click()
time.sleep(3)  # Esperar a que la página cargue

# Marcar XIAOMI
xiaomi = bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div[2]/div/ul/li[3]/div/ul/li[1]/label/input")
xiaomi.click()
time.sleep(6)  # Espera que recargue

# Volver a abrir sección Marca
marca_btn = bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div[3]/div/ul/li[2]/button")
bot.execute_script("arguments[0].scrollIntoView();", marca_btn)
time.sleep(3)
marca_btn.click()
time.sleep(3)

# Marcar LENOVO
lenovo = bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div[3]/div/ul/li[2]/div/ul/li[2]/label/input")
lenovo.click()
time.sleep(6)

# Extraer datos desde el script "__NEXT_DATA__"
productos = []

try:
    script = bot.find_element(By.XPATH, "/html/body/script[@id='__NEXT_DATA__']")
    contenido = script.get_attribute("innerHTML")
    data = json.loads(contenido)

    productos_data = data["props"]["pageProps"]["results"]

    for prod in productos_data:
        nombre = prod.get("displayName", "Sin nombre")
        url = prod.get("url", "#")
        enlace = url if url.startswith("http") else f"https://www.falabella.com.co{url}"
        
        # Buscar el primer precio (puede haber varios en la lista)
        try:
            precio = prod["prices"][0]["price"][0]
        except:
            precio = "Sin precio"

        productos.append({
            "nombre": nombre,
            "precio": f"$ {precio}",
            "enlace": enlace
        })

    print(f"Productos extraídos desde JSON: {len(productos)}")

except Exception as e:
    print("Error al obtener datos desde __NEXT_DATA__:", str(e))

# Guardar en CSV
with open("auriculares_falabella.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    columnas = ["nombre", "precio", "enlace"]
    writer = csv.DictWriter(archivo_csv, fieldnames=columnas)
    writer.writeheader()
    for producto in productos:
        writer.writerow(producto)

# Guardar en JSON solo los precios
precios = {"precios": [producto["precio"] for producto in productos]}

with open("precios_auriculares.json", "w", encoding="utf-8") as archivo_json:
    json.dump(precios, archivo_json, indent=4, ensure_ascii=False)


try:
    # Hacer scroll hasta el final de la página
    bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    instagram_icon = bot.find_element(By.XPATH, "/html/body/div[1]/footer/section[2]/div/div[1]/ul/li[2]/a")
    instagram_icon.click()
    print("Se hizo clic en el ícono de Instagram.")
    time.sleep(5)  # Esperar que cargue la página

    # Tomar una captura de pantalla
    bot.save_screenshot("screenshot_instagram.png")
    print("Captura de pantalla guardada como screenshot_instagram.png.")

except Exception as e:
    print("Error al intentar acceder al ícono de Instagram o tomar el screenshot:", str(e))




bot.quit()  # Cerrar el navegador


