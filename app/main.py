import os
from datetime import datetime
from app.agents.navegador import navegar_para_urls
from app.agents.analise import extrair_dados_vagas
from app.agents.formatador import gerar_markdown
from app.agents.vaga_matcher import VagaMatcher
from app.agents.proposta_generator import PropostaGenerator
from app.agents.freelancing_expert import FreelancingExpert

def carregar_historico():
    with open("historico.md", "r", encoding="utf-8") as file:
        return file.read()

def executar_fluxo():
    historico = carregar_historico()
    
    html_list = navegar_para_urls()
    
    vagas = []
    for html in html_list:
        vagas.extend(extrair_dados_vagas(html))

    resultados = []
    
    matcher = VagaMatcher()
    gerador = PropostaGenerator()
    expert = FreelancingExpert()

    for vaga in vagas:
        job_description = f"{vaga['titulo']}\nDescrição: {vaga['descricao']}\nOrçamento: {vaga['orcamento']}\n{vaga['link']}"

        analise_resultado = matcher.analyze(job_description, historico)
        # print(f"Resultado da análise: {analise_resultado}")
        
        if "SIM" in analise_resultado.upper():
            proposta = gerador.generate(job_description)
            # review = expert.review(job_description, proposta)
            
            resultados.append({
                "titulo": vaga["titulo"],
                "link": vaga["link"],
                "publicacao": vaga["publicacao"],
                "propostas": vaga["propostas"],
                "prazo": vaga["prazo"],
                "orcamento": vaga["orcamento"],
                # "habilidades": vaga["habilidades"],
                "analise": analise_resultado,
                "proposta": proposta,
                # "review": review
            })

    markdown_output = gerar_markdown(resultados)
    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f'vagas_analysis_{timestamp}.md')
    
    # Save markdown output to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_output)
    
    print(f"Results saved to: {output_file}")
    print(markdown_output)

if __name__ == "__main__":
    executar_fluxo()
