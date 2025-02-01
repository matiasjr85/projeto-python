from src.factory.llm_factory import LLMFactory

class ChatCommand:
    """Comando para enviar perguntas aos modelos"""

    def __init__(self, connection):
        self.connection = connection

    def execute(self, prompt):
        return self.connection.send_query(prompt)