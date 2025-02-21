import os
from datetime import datetime
from crewai import Agent  # integração com a CrewAI
from openai import OpenAI

client = OpenAI()
from app.database import salvar_log

class VagaMatcher(Agent):
    def __init__(self):
        super().__init__(
            role="Especialista em Correspondência de Vagas",
            goal="Analisar se uma vaga de trabalho é compatível com o histórico profissional do usuário.",
            backstory="Um especialista em recrutamento freelancer que já analisou centenas de oportunidades para candidatos em tecnologia.",
        )

    def analyze(self, job_description, historico):
        prompt = (
            f"Meu histórico profissional é:\n{historico}\n\n"
            f"Analise a seguinte descrição de vaga e responda apenas com SIM ou NÃO, "
            f"acompanhado de uma breve justificativa: {job_description}"
        )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
        salvar_log("vaga_matcher", f"Análise da vaga {job_description}: {result}")
        
         # Create logs directory if it doesn't exist
        log_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'logs')
        os.makedirs(log_dir, exist_ok=True)
        
        # Define the markdown file path
        md_file = os.path.join(log_dir, 'job_analysis.md')
        
        # Format the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format the markdown entry
        md_entry = f"""
## Job Analysis - {current_time}

### Job Description
{job_description}

### Analysis Result
{result}

---
        """
        
        # Append or create the markdown file
        with open(md_file, 'a', encoding='utf-8') as f:
            f.write(md_entry)
        
        return result
