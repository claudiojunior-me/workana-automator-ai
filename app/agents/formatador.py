def gerar_markdown(resultados):
    md = "# Resultados do Projeto\n\n"
    
    for resultado in resultados:
        md += f"## {resultado['titulo']}\n"
        md += f"- **Link:** {resultado['link']}\n"
        md += f"- **Publicação:** {resultado['publicacao']}\n"
        md += f"- **Propostas:** {resultado['propostas']}\n"
        md += f"- **Prazo:** {resultado['prazo']}\n"
        md += f"- **Orçamento:** {resultado['orcamento']}\n"
        md += "### Análise da Vaga:\n"
        md += f"{resultado['analise']}\n"
        md += "### Proposta:\n"
        md += f"{resultado['proposta']}\n\n"
        md += "\n\n---\n\n"
    return md
