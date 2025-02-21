BASE_URL = "https://www.workana.com/jobs"

def construir_urls(categorias, subcategorias, periodo="3d", idioma="pt"):
    urls = []
    for categoria in categorias:
        url = f"{BASE_URL}?category={categoria}&language={idioma}&publication={periodo}"
        # url = f"{BASE_URL}?category={categoria}&language={idioma}&publication={periodo}&subcategory={','.join(subcategorias)}"
        urls.append(url)
    return urls
