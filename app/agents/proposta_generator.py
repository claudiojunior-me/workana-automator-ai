from crewai import Agent
from openai import OpenAI

client = OpenAI()
from app.database import salvar_log

class PropostaGenerator(Agent):
    def __init__(self):
        super().__init__(
            role="Gerador de Propostas Freelance",
            goal="Criar uma proposta personalizada para a vaga com base nos requisitos e no histórico do usuário.",
            backstory="Um redator de propostas freelancer com anos de experiência, especializado em convencer clientes e fechar negócios.",
        )
    
    def generate(self, job_description):
        prompt = (
            f"Baseando-se na seguinte descrição de vaga:\n{job_description}\n\n"
            f"e seguindo o padrão de proposta de trabalho freelance, "
            f"gere uma proposta detalhada e profissional."
        )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        proposta = response.choices[0].message.content
        salvar_log("proposta_generator", "Proposta gerada com sucesso.")
        return proposta
