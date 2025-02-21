from bs4 import BeautifulSoup
from app.database import salvar_log
from app.agents.navegador import navegar_para_urls
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.workana.com"

def extrair_dados_vagas(html):
    soup = BeautifulSoup(html, 'html.parser')
    projetos_div = soup.find("div", id="projects")

    if not projetos_div:
        salvar_log("erro", "Nenhuma vaga encontrada.")
        return []

    vagas = []
    for projeto in projetos_div.find_all("div", class_="project-item"):
        try:
            titulo_tag = projeto.find("h2", class_="h3 project-title").find("a")
            titulo = titulo_tag.get_text(strip=True)
            link = BASE_URL + titulo_tag["href"]

            publicacao_tag = projeto.find("h5", class_="date")
            publicacao = publicacao_tag.get_text(strip=True) if publicacao_tag else "Desconhecido"

            propostas_tag = projeto.find("span", class_="bids")
            propostas = propostas_tag.get_text(strip=True) if propostas_tag else "0 propostas"

            prazo_tag = projeto.find("span", class_="deadline").find("span", class_="value") if projeto.find("span", class_="deadline") else None
            prazo = prazo_tag.get_text(strip=True) if prazo_tag else "Sem prazo"

            descricao, orcamento = extrair_detalhes_vaga(link)

            print(f"Extraída vaga: {titulo}, {link}")

            vagas.append({
                "titulo": titulo,
                "link": link,
                "publicacao": publicacao,
                "propostas": propostas,
                "prazo": prazo,
                "descricao": descricao,
                # "habilidades": habilidades,
                "orcamento": orcamento
            })

        except Exception as e:
            salvar_log("erro", f"Erro ao extrair dados: {str(e)}")

    salvar_log("extracao", f"Extraídas {len(vagas)} vagas.")
    return vagas

def extrair_detalhes_vaga(link):
    """ Acessa a página da vaga e extrai a descrição e habilidades usando Selenium. """
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get(link)
        
        # Wait for the content to load
        driver.implicitly_wait(5)
        
        # Get page source and create BeautifulSoup object
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Extract description
        descricao_tag = soup.find("div", class_="expander js-expander-passed")
        descricao = descricao_tag.get_text(strip=True) if descricao_tag else "Descrição não encontrada."
        
        # Extract budget
        orcamento_tag = soup.find("h4", class_="budget")
        orcamento = orcamento_tag.get_text(strip=True) if orcamento_tag else "Orçamento não informado"
        
        driver.quit()
        return descricao, orcamento
        
    except Exception as e:
        salvar_log("erro", f"Erro ao acessar detalhes da vaga: {str(e)}")
        if 'driver' in locals():
            driver.quit()
        return "Erro ao acessar descrição", "Erro ao acessar orçamento"
