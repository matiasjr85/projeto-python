class EvaluationStrategy:
    """Classe base para todas as estratégias de avaliação"""

    def evaluate(self, response1, response2, **kwargs):
        """Deve ser implementado pelas classes filhas"""
        raise NotImplementedError("Método 'evaluate' deve ser implementado.")
