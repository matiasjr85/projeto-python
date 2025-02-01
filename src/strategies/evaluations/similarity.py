from difflib import SequenceMatcher
from strategies.base import EvaluationStrategy

class SimilarityEvaluation(EvaluationStrategy):
    """Avalia a resposta mais parecida com a pergunta"""

    def evaluate(self, response1, response2, **kwargs):
        prompt = kwargs.get("prompt", "")

        # 🔥 GARANTE QUE AS RESPOSTAS SEJAM STRINGS
        response1_text = str(response1) if isinstance(response1, str) else str(response1.get("text", ""))
        response2_text = str(response2) if isinstance(response2, str) else str(response2.get("text", ""))

        # 🔥 VERIFICA SE A RESPOSTA É UM ERRO (exemplo: {'error': '401 Unauthorized'})
        if "error" in response1_text.lower():
            response1_text = ""
        if "error" in response2_text.lower():
            response2_text = ""

        similarity1 = SequenceMatcher(None, prompt, response1_text).ratio()
        similarity2 = SequenceMatcher(None, prompt, response2_text).ratio()

        return response1_text if similarity1 > similarity2 else response2_text
