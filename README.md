# 🌎🤖 GeoAI Mentor

Chatbot desenvolvido em **Python** utilizando **LangChain** e a **API da OpenAI**, com gerenciamento de histórico para manter o contexto entre diferentes mensagens de uma mesma sessão.

O projeto foi desenvolvido durante o **Checkpoint Especialista em IA – Nível 1**, da Alura, como aplicação prática dos conceitos estudados.

---

## 🎯 Objetivo

Criar um assistente de Inteligência Artificial especializado em orientar geocientistas interessados em migrar para a área de Ciência de Dados.

O chatbot utiliza um prompt de sistema para definir seu comportamento e mantém o histórico da conversa, permitindo que perguntas posteriores sejam respondidas considerando o contexto das mensagens anteriores.

---

## ⚙️ Como funciona

O fluxo principal da aplicação é:

`Pergunta → Prompt → Histórico da sessão → Modelo OpenAI → Parser → Resposta`

A aplicação utiliza uma `Chain` do LangChain composta por:

- `ChatPromptTemplate`
- `ChatOpenAI`
- `StrOutputParser`

O histórico das conversas é armazenado em memória utilizando:

- `InMemoryChatMessageHistory`
- `RunnableWithMessageHistory`

Cada conversa é identificada por um `session_id`, permitindo recuperar o histórico correspondente durante a execução.

---

## 🛠️ Tecnologias utilizadas

- Python
- LangChain
- LangChain OpenAI
- OpenAI API
- python-dotenv

---

## 🧠 Conceitos praticados

Durante o desenvolvimento foram aplicados conceitos como:

- Integração com modelos da OpenAI
- Prompt Engineering
- ChatPromptTemplate
- Chains com LangChain
- Output Parsers
- Memória de conversação
- Gerenciamento de sessões
- Variáveis de ambiente
- Gerenciamento seguro de chaves de API

---

## 💬 Exemplo de interação

O projeto utiliza perguntas sequenciais como:

**Pergunta 1:**

> Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?

**Pergunta 2:**

> E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?

A segunda pergunta utiliza o histórico da mesma sessão, permitindo que o modelo considere o contexto estabelecido anteriormente.

---

## 📂 Estrutura do projeto

```text
.
├── chatbot_mentor.py
├── requirements.txt
├── .gitignore
└── README.md
