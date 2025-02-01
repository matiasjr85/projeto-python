from strategies.base import EvaluationStrategy

class LengthEvaluation(EvaluationStrategy):
    """Avaliação pela resposta mais longa"""

    def evaluate(self, response1, response2, **kwargs):
        return response1 if len(response1) > len(response2) else response2
