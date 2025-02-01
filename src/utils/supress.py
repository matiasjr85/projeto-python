import os
import sys
from contextlib import contextmanager
from transformers.utils.logging import set_verbosity_error
from transformers import AutoTokenizer, AutoModelForQuestionAnswering


set_verbosity_error()  # 🔥 Reduz verbosidade

@contextmanager
def suppress_stdout():
    """Suprime saída padrão temporariamente"""
    with open(os.devnull, "w") as fnull:
        old_stdout = sys.stdout
        sys.stdout = fnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

# Suprime logs enquanto carrega os modelos
with suppress_stdout():
    tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
    model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
