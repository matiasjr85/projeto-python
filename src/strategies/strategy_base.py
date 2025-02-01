from strategies.evaluations.length import LengthEvaluation
from strategies.evaluations.similarity import SimilarityEvaluation
from strategies.evaluations.readability import ReadabilityEvaluation
from strategies.evaluations.sentiment import SentimentEvaluation
from strategies.evaluations.relevance import RelevanceEvaluation

from strategies.advanced.coherence import CoherenceEvaluation
from strategies.advanced.factuality import FactualityEvaluation
from strategies.advanced.context_awareness import ContextAwarenessEvaluation
from strategies.advanced.grammar import GrammarEvaluation
from strategies.advanced.engagement import EngagementEvaluation

# Lista com todas as estratégias
ALL_STRATEGIES = [
    LengthEvaluation(),
    SimilarityEvaluation(),
    ReadabilityEvaluation(),
    SentimentEvaluation(),
    RelevanceEvaluation(),
    CoherenceEvaluation(),
    FactualityEvaluation(),
    ContextAwarenessEvaluation(),
    GrammarEvaluation(),
    EngagementEvaluation()
]
