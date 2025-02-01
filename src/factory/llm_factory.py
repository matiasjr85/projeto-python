from src.models.chatgpt import ChatGPTConnection
from src.models.roberta import RoBERTaLLM

class LLMFactory:
    @staticmethod
    def get_connection(model_name):
        """Retorna a conexão correta baseada no modelo"""
        if model_name == "chatgpt":
            return ChatGPTConnection()
        elif model_name == "roberta":
            return RoBERTaLLM()
        else:
            raise ValueError(f"Modelo {model_name} não reconhecido.")
