import requests
from strategies.base import EvaluationStrategy

class FactualityEvaluation(EvaluationStrategy):
    """Verifica se a resposta contém informações factuais com base em APIs externas"""

    def evaluate(self, response1, response2, **kwargs):
        search_api_url = "https://api.duckduckgo.com/?q={}&format=json"
        
        # Simula verificação factual buscando no DuckDuckGo
        query = kwargs.get("prompt", "")
        response = requests.get(search_api_url.format(query)).json()
        
        factual1 = sum(1 for phrase in response1.split() if phrase.lower() in str(response))
        factual2 = sum(1 for phrase in response2.split() if phrase.lower() in str(response))

        return response1 if factual1 > factual2 else response2