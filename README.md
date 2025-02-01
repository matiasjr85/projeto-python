# Chatbot com Múltiplos LLMs

## 📌 Visão Geral

Este projeto é um chatbot baseado em múltiplos Modelos de Linguagem de Grande Escala (LLMs), utilizando integrações com OpenAI e Hugging Face APIs. 

O objetivo é fornecer um chatbot flexível e altamente configurável para aplicações diversas, desde assistentes virtuais até suporte automatizado.

## 📌 Tecnologias Utilizadas

- **Linguagem:** Python
- **Frameworks e Bibliotecas:**
  - OpenAI API
  - Hugging Face API (RoBERTa)
  - Uvicorn
  - Transformers
  - PyTorch
  - Testes com Pytest
  - Integração com LanguageTool para correção gramatical

## 📌 Padrões de Projeto Implementados

- **Factory**: Para criação de objetos de conexão com diferentes APIs de LLMs.
- **Command**: Para encapsular solicitações do usuário e permitir flexibilidade na execução de diferentes comandos.
- **Strategy**: Para permitir a comparação das respostas dos modelos usando diferentes critérios de avaliação.
- **Observer**: Para notificar e atualizar automaticamente a interface sobre mudanças nas respostas escolhidas.

## 📌 Estrutura do Projeto

```
📂 projeto_chatbot/
├── 📂 config/          # Arquivos de configuração
│   ├── __init__.py
│   ├── config.py
│   ├── 📂 __pycache__/
├── 📂 logs/            # Diretório de logs
│   ├── __init__.py
│   ├── chatbot.log
│   ├── chat_history.txt
├── 📂 src/             # Código-fonte principal
│   ├── __init__.py
│   ├── 📂 cli/
│   │   ├── __init__.py
│   │   ├── chatbot_cli.py
│   ├── 📂 models/      # Modelos e processamento de linguagem natural
│   │   ├── __init__.py
│   │   ├── chatgpt.py
│   │   ├── roberta.py
│   ├── 📂 strategies/
│   │   ├── __init__.py
│   │   ├── strategy_base.py
│   ├── 📂 factory/
│   │   ├── __init__.py
│   │   ├── llm_factory.py
│   ├── 📂 observers/
│   │   ├── __init__.py
│   │   ├── observer.py
│   ├── 📂 utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   ├── 📂 tests/
│   │   ├── __init__.py
├── 📄 requirements.txt # Dependências do projeto
├── 🚀 run.py           # Script principal de execução
├── 📖 README.md        # Documentação
```

## 📌 Instalação e Execução

### 1️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Rodar o chatbot via CLI

```bash
python src/cli/chatbot_cli.py
```

### 3️⃣ Executar testes

```bash
pytest
```

### 4️⃣ Rodar o projeto principal

```bash
python run.py
```

## 📌 Arquitetura do Sistema

O projeto segue uma arquitetura modular com os seguintes componentes principais:

```
+----------------------+
|     Usuário         |
+----------------------+
           |
           v
+----------------------+       +----------------------+
| Interface CLI        | ----> | OpenAI / RoBERTa     |
+----------------------+       +----------------------+
           |
           v
+----------------------+
|  Logs e Monitoramento |
+----------------------+
```

- **Interface CLI**: Permite interagir com o chatbot via terminal.
- **Mecanismo de Modelos**: Permite utilizar diferentes LLMs (OpenAI, RoBERTa).
- **Comparação de Respostas**: Implementada via Strategy Pattern.
- **Notificação Automática**: Implementada com Observer Pattern.
- **Testes Automatizados**: Garantem a qualidade e robustez do código.
- **Docker e Kubernetes**: Facilita a implantação escalável do chatbot.

## 📌 Dependências Principais

As dependências do projeto estão listadas no `requirements.txt` e incluem:

```
openai
requests
textstat
uvicorn
pytest
python-dotenv
textblob
language_tool_python
transformers
torch
```

## 📌 Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para sua feature: `git checkout -b minha-feature`
3. Faça commit das mudanças: `git commit -m 'Adicionando minha feature'`
4. Envie para o repositório remoto: `git push origin minha-feature`
5. Abra um Pull Request.

## 📌 Contato

Caso tenha dúvidas ou sugestões, entre em contato com o time de desenvolvimento.

---

Este README foi gerado para fornecer uma visão abrangente do projeto e facilitar sua utilização e desenvolvimento!

