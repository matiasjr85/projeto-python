# Chatbot com Múltiplos LLMs

## 📌 Visão Geral

Este projeto é um chatbot baseado em múltiplos Modelos de Linguagem de Grande Escala (LLMs), utilizando integrações com OpenAI e Hugging Face APIs. 

O objetivo é fornecer um chatbot flexível e altamente configurável para aplicações diversas, desde assistentes virtuais até suporte automatizado.

## 📌 📺 Vídeo Tutorial

Para um guia detalhado sobre a instalação e uso do projeto, assista ao vídeo tutorial no YouTube:

[![Tutorial do Chatbot](https://img.youtube.com/vi/mhsykWUaqmI/maxresdefault.jpg)](https://www.youtube.com/watch?v=mhsykWUaqmI)


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
├── 📂 logs/            # Diretório de logs
├── 📂 src/             # Código-fonte principal
│   ├── 📂 cli/         # Interface via terminal
│   ├── 📂 models/      # Modelos e processamento de linguagem natural
│   ├── 📂 strategies/  # Estratégias de decisão
│   ├── 📂 factory/     # Fábrica de LLMs
│   ├── 📂 observers/   # Implementação do padrão Observer
│   ├── 📂 utils/       # Utilitários e logs
│   ├── 📂 tests/       # Testes automatizados
├── 📄 requirements.txt # Dependências do projeto
├── 🚀 run.py           # Script principal de execução
├── 📖 README.md        # Documentação
```

## 📌 Instalação e Execução

### 1️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Configurar variáveis de ambiente (.env)

Antes de rodar o projeto, **é necessário criar um arquivo `.env` na pasta principal do projeto** com as seguintes variáveis:

```
OPENAI_API_KEY=******
HUGGINGFACE_API_TOKEN=******
```

Essas chaves são essenciais para autenticação nas APIs do OpenAI e Hugging Face.

### 3️⃣ Rodar o chatbot via CLI

```bash
python src/cli/chatbot_cli.py
```

### 4️⃣ Executar testes

```bash
pytest
```

### 5️⃣ Rodar o projeto principal

```bash
python run.py
```

## 📌 Observação Importante

- O projeto **exige a configuração do arquivo `.env`** com as credenciais das APIs para funcionar corretamente.
- Certifique-se de ter acesso às **APIs da OpenAI e Hugging Face**, pois chamadas não autenticadas resultarão em erro.
- Se estiver enfrentando **problemas de GPU**, experimente rodar o modelo na CPU alterando as configurações no código.

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

Este README foi atualizado para incluir o **vídeo tutorial**, **informações sobre o .env**, e **observações importantes** para facilitar o uso do projeto! 🚀
