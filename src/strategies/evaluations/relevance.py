from strategies.base import EvaluationStrategy

class RelevanceEvaluation(EvaluationStrategy):
    """Avaliador de relevância baseada na presença de palavras-chave"""

    def evaluate(self, response1, response2, **kwargs):
        prompt = kwargs.get("prompt", "").lower()
        relevance1 = sum(1 for word in prompt.split() if word in response1.lower())
        relevance2 = sum(1 for word in prompt.split() if word in response2.lower())
        return response1 if relevance1 > relevance2 else response2
