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
            f"[Input]"
            f"sobre minha carreira: Com mais de 10 anos de experiência em desenvolvimento de interfaces web, construí uma trajetória sólida criando soluções eficientes e escaláveis. Na Luizalabs, meu atual emprego, fui responsável por projetar e implementar um e-commerce B2B que hoje atende mais de 100 mil usuários diários, destacando-me pela liderança em decisões arquiteturais e tecnológicas, sempre priorizando performance, segurança e responsividade. Tenho profundo domínio em React, TypeScript e ferramentas de testes como Jest, garantindo a entrega de código de alta qualidade. "
            f"nível de cargo: front-end senior "
            f"valor por hora: R$ 80 "
            f"expertise: Javascript, Typescript, React, Node, Docker, CSS "
            f"horários disponível para freelance: 19:00 ás 23:00 segunda a sexta, 13:00 ás 21:00 sábado e domingo. "
            f"sobre o freelance: {job_description}"
            f"[Output] "
            f"- **Nome:** Claudio Vasconcelos Junior "
            f"- **Calcule quanto tempo você levará para realizar o projeto:** "
            f"- **Descreva sua experiência em projetos similares:** "
            f"- **Defina de quais informações você precisa para começar:** "
            f"- **Explique porque você é o candidato ideal:** "
            f"- **Horas de trabalho:** ... horas "
            f"- **Preço por hora:** R$"
            f"- **Detalhes da proposta:** "
            f"- **De quanto tempo você precisa para finalizar o trabalho?** ... dias"
        )
        # prompt = (
        #     f"Baseando-se na seguinte descrição de vaga:\n{job_description}\n\n"
        #     f"e seguindo o padrão de proposta de trabalho freelance, "
        #     f"gere uma proposta detalhada e profissional."
        # )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        proposta = response.choices[0].message.content
        salvar_log("proposta_generator", "Proposta gerada com sucesso.")
        return proposta
