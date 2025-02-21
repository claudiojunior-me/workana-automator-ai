from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.database import salvar_log
from app.agents.url_builder import construir_urls

CATEGORIAS = ["it-programming", "design-multimedia", "admin-support", "writing-translation"]
SUBCATEGORIAS = [
    "web-development", "web-design", "e-commerce"
]

def navegar_para_urls():
    urls = construir_urls(CATEGORIAS, SUBCATEGORIAS)
    
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    all_html = []
    for url in urls:
        driver.get(url)
        salvar_log("navegacao", f"Acessou a URL: {url}")
        all_html.append(driver.page_source)
    
    driver.quit()
    return all_html
