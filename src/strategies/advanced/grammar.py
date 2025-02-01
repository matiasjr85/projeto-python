import language_tool_python
from strategies.base import EvaluationStrategy

class GrammarEvaluation(EvaluationStrategy):
    """Avalia qual resposta tem menos erros gramaticais"""

    def evaluate(self, response1, response2, **kwargs):
        tool = language_tool_python.LanguageTool('en-US')

        errors1 = len(tool.check(response1))
        errors2 = len(tool.check(response2))

        return response1 if errors1 < errors2 else response2
