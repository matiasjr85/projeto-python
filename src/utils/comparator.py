from src.utils.colors import Colors
from src.strategies.strategy_base import ALL_STRATEGIES

def compare_responses(prompt, response1, response2, context=""):
    """Aplica estratégias para determinar a melhor resposta"""
    
    response1_text = str(response1) if isinstance(response1, str) else str(response1.get("text", ""))
    response2_text = str(response2) if isinstance(response2, str) else str(response2.get("text", ""))

    if "error" in response1_text.lower():
        response1_text = "Erro na resposta do ChatGPT"
    if "error" in response2_text.lower():
        response2_text = "Erro na resposta da RoBERTa"

    scores = {response1_text: 0, response2_text: 0}
    strategy_results = {}

    print(Colors.OKCYAN + "\n📊 Comparação das Respostas:" + Colors.ENDC)
    print(Colors.OKBLUE + f"🔹 ChatGPT: {response1_text}" + Colors.ENDC)
    print(Colors.OKGREEN + f"🔹 RoBERTa: {response2_text}" + Colors.ENDC)

    for strategy in ALL_STRATEGIES:
        best = strategy.evaluate(response1_text, response2_text, prompt=prompt, context=context)
        scores[best] += 1
        strategy_results[strategy.__class__.__name__] = "ChatGPT" if best == response1_text else "RoBERTa"

    final_response = max(scores, key=scores.get)

    print(Colors.BOLD + "\n🏆 Resumo das Estratégias:" + Colors.ENDC)
    for strategy, winner in strategy_results.items():
        print(f"✔️ {strategy}: {winner}")

    return final_response
