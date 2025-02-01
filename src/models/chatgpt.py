import openai
from config.config import OPENAI_API_KEY

class ChatGPTConnection:
    """Conexão com a API do ChatGPT"""

    def send_query(self, prompt: str, temperature=0.7) -> str:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,  # 🔥 Ajuste de criatividade
            max_tokens=200
        )

        return response.choices[0].message.content
