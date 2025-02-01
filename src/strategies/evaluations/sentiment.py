from textblob import TextBlob
from strategies.base import EvaluationStrategy

class SentimentEvaluation(EvaluationStrategy):
    """Avalia qual resposta tem um tom mais positivo"""

    def evaluate(self, response1, response2, **kwargs):
        sentiment1 = TextBlob(response1).sentiment.polarity
        sentiment2 = TextBlob(response2).sentiment.polarity
        return response1 if sentiment1 > sentiment2 else response2
