from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import torch
from transformers.utils.logging import set_verbosity_error


class RoBERTaLLM:
    def __init__(self):
        set_verbosity_error()

        """Carrega o modelo RoBERTa otimizado para QA"""
        model_name = "deepset/roberta-base-squad2"
        print("🔄 Carregando IAs, aguarde...")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name)

        self.qa_pipeline = pipeline("question-answering", model=model_name, tokenizer=model_name)

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def send_query(self, question):
        """Executa uma consulta no modelo RoBERTa"""
        context = """
        RoBERTa é um modelo de Processamento de Linguagem Natural (NLP) desenvolvido pela Facebook AI.
        Ele é baseado no BERT, mas foi treinado de forma mais robusta para melhorar o entendimento contextual.
        Atualmente, pode ser usado para tarefas como análise de sentimentos, resposta a perguntas e preenchimento de lacunas.
        """

        try:
            result = self.qa_pipeline(question=question, context=context)
            return result["answer"]
        except Exception as e:
            return f"Erro ao processar RoBERTa: {e}"
