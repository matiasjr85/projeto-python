from src.factory.llm_factory import LLMFactory
from src.commands.chat_command import ChatCommand
from src.observers.observer import ResponseNotifier, Observer
from src.utils.colors import Colors
from src.utils.logger import log_error
from src.utils.history import save_interaction, load_history
from src.utils.effects import type_effect
from src.utils.comparator import compare_responses

notifier = ResponseNotifier()
observer = Observer()
notifier.add_observer(observer)

def show_history():
    """Exibe o histórico de conversas"""
    history = load_history()
    if history:
        print(Colors.OKCYAN + "\n📖 Histórico de Conversas:\n" + Colors.ENDC)
        print("".join(history))
    else:
        print(Colors.WARNING + "🔹 Nenhuma conversa registrada ainda." + Colors.ENDC)

def chatbot_cli():
    print(Colors.HEADER + "🔥 Bem-vindo ao Chatbot Inteligente! 🔥\n" + Colors.ENDC)

    try:
        chatgpt_conn = LLMFactory.get_connection("chatgpt")
        roberta_conn = LLMFactory.get_connection("roberta")
        chatgpt_cmd = ChatCommand(chatgpt_conn)
        roberta_cmd = ChatCommand(roberta_conn)
        
        print(Colors.OKGREEN + "💡 DICA: Digite 'contexto' e veja seu histórico de iteração." + Colors.ENDC)
        
        print("✅ IAs Online!")
        
        while True:
            print(Colors.OKBLUE + "\n💬 Digite sua pergunta (ou 'sair' para finalizar): " + Colors.ENDC, end="")
            prompt = input().strip()

            if prompt.lower() == "sair":
                print(Colors.WARNING + "👋 Encerrando o chatbot. Até mais!\n" + Colors.ENDC)
                break
            elif prompt.lower() == "contexto":
                show_history()
                continue

            print(Colors.OKCYAN + "⏳ Consultando IA... Aguarde...\n" + Colors.ENDC)
            
            response_chatgpt = chatgpt_cmd.execute(prompt)
            response_roberta = roberta_cmd.execute(prompt)

            final_response = compare_responses(prompt, response_chatgpt, response_roberta)

            print(Colors.BOLD + "\n💡 Resposta Final: " + Colors.ENDC, end="")
            type_effect(final_response)

            save_interaction(prompt, final_response)

    except ValueError as e:
        log_error(f"Erro no chatbot: {e}")
        print(Colors.FAIL + f"❌ Erro: {e}" + Colors.ENDC)

if __name__ == "__main__":
    chatbot_cli()
