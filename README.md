#  GeoAI Mentor

Projeto desenvolvido durante a formação **Especialista em IA** da Alura.

O objetivo é criar um chatbot utilizando **Python**, **LangChain** e a **API da OpenAI**, capaz de responder perguntas mantendo o contexto da conversa por meio de memória de sessão.

## Tecnologias

- Python
- LangChain
- OpenAI
- python-dotenv

## Como executar

1. Clone este repositório.
2. Crie e ative um ambiente virtual.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto:

```text
OPENAI_API_KEY="SUA_CHAVE"
```

5. Execute o projeto:

```bash
python chatbot_mentor.py
```

## O que foi praticado

- Uso da API da OpenAI
- Criação de prompts com LangChain
- Organização de uma Chain
- Memória de conversa utilizando `RunnableWithMessageHistory`
- Gerenciamento seguro da chave da API com `.env`

## Observação

Para executar o chatbot é necessário possuir uma chave da OpenAI com créditos disponíveis. Caso contrário, a API retornará o erro `429 - insufficient_quota`.