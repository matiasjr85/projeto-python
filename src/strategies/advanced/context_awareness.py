from strategies.base import EvaluationStrategy

class ContextAwarenessEvaluation(EvaluationStrategy):
    """Avalia qual resposta mantém melhor a continuidade do contexto"""

    def evaluate(self, response1, response2, **kwargs):
        context = kwargs.get("context", "").split()
        score1 = sum(1 for word in response1.split() if word in context)
        score2 = sum(1 for word in response2.split() if word in context)

        return response1 if score1 > score2 else response2
