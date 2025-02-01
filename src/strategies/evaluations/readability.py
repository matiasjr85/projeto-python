import textstat
from strategies.base import EvaluationStrategy

class ReadabilityEvaluation(EvaluationStrategy):
    """Avaliação da resposta mais fácil de ler"""

    def evaluate(self, response1, response2, **kwargs):
        score1 = textstat.flesch_reading_ease(response1)
        score2 = textstat.flesch_reading_ease(response2)
        return response1 if score1 > score2 else response2
