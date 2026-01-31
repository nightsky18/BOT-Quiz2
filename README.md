# WebScraper Falabella
Este bot automatiza la búsqueda de productos en el sitio web de Falabella Colombia, utilizando el navegador Google Chrome controlado por Selenium WebDriver

## Funcionalidades

1. Accede al sitio web [falabella.com.co](https://www.falabella.com.co/)
2. Realiza la búsqueda: `Auriculares inalámbricos`.
3. Aplica filtros de marca: `XIAOMI` y `LENOVO`.
4. Extrae datos de los productos directamente desde el JSON de la página (`__NEXT_DATA__`).
5. Guarda:
   - Un archivo CSV con nombre, precio y enlace de cada producto.
   - Un archivo JSON con la lista de precios.
6. Accede al ícono de Instagram desde el footer de la página y toma un pantallazo.

## Requisitos
Tener instalado
- Python 3.10 o superior
- Google Chrome
- ChromeDriver compatible con tu versión de Chrome
- Selenium
