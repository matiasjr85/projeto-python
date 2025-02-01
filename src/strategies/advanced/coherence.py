from strategies.base import EvaluationStrategy

class CoherenceEvaluation(EvaluationStrategy):
    """Avalia qual resposta tem melhor coerência interna"""

    def evaluate(self, response1, response2, **kwargs):
        coherence1 = response1.count('.')  # Número de frases pode indicar coerência
        coherence2 = response2.count('.')
        return response1 if coherence1 > coherence2 else response2
