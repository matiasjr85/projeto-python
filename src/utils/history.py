import os
import datetime

# Diretório para armazenar os logs
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "chat_history.txt")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def save_interaction(question, response):
    """Salva interações no histórico de conversas"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Pergunta: {question}\n[{timestamp}] Resposta: {response}\n\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def load_history():
    """Carrega o histórico de conversas"""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    return []
