def gerar_markdown(resultados):
    md = "# Resultados do Projeto\n\n"
    for resultado in resultados:
        md += f"- **Link:** {resultado['link']}\n"
        md += f"  - **Análise da Vaga:** {resultado['analise']}\n"
        md += f"  - **Proposta:** {resultado['proposta']}\n"
        md += f"  - **Revisão (Expert):** {resultado['review']}\n\n"
    return md
