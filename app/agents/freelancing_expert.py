from crewai import Agent
from openai import OpenAI

client = OpenAI()
from app.database import salvar_log

class FreelancingExpert(Agent):
    def __init__(self):
        super().__init__(
            role="Especialista em Freelancing",
            goal="Revisar a descrição da vaga e a proposta gerada para garantir que atendem aos padrões do mercado freelancer.",
            backstory="Um consultor experiente que já ajudou centenas de freelancers a conseguir os melhores contratos em plataformas como Workana e Upwork.",
        )
    
    def review(self, job_description, proposta):
        prompt = (
            f"Revise a descrição da vaga:\n{job_description}\n\n"
            f"E a proposta a seguir:\n{proposta}\n\n"
            f"Forneça feedback e sugestões para alinhar a proposta à vaga."
        )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        review = response.choices[0].message.content
        salvar_log("freelancing_expert", "Revisão da proposta concluída.")
        return review
