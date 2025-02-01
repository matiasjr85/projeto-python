from strategies.base import EvaluationStrategy

class EngagementEvaluation(EvaluationStrategy):
    """Avalia qual resposta tem maior potencial de engajamento"""

    def evaluate(self, response1, response2, **kwargs):
        engagement1 = response1.count("!") + response1.count("?")
        engagement2 = response2.count("!") + response2.count("?")

        return response1 if engagement1 > engagement2 else response2
