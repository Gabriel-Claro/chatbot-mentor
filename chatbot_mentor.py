import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


load_dotenv()


chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)


perguntas = [
    "Eu sou geofísico e quero migrar para a área de dados. "
    "Qual linguagem de programação devo aprender primeiro?",

    "E que tipo de projeto de portfólio eu poderia criar "
    "usando essa linguagem?"
]


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Você é o 'GeoAI Mentor', um assistente especializado em ajudar "
            "geocientistas a migrar para a área de Ciência de Dados. "
            "Seja amigável e didático."
        ),
        ("placeholder", "{historico}"),
        ("human", "{query}")
    ]
)


chain = prompt | chat | StrOutputParser()


memoria_sessoes = {}


def obter_historico_por_sessao(
    session_id: str
) -> InMemoryChatMessageHistory:

    if session_id not in memoria_sessoes:
        memoria_sessoes[session_id] = InMemoryChatMessageHistory()

    return memoria_sessoes[session_id]


cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico"
)


for pergunta in perguntas:
    resposta = cadeia_com_memoria.invoke(
        {
            "query": pergunta
        },
        config={
            "configurable": {
                "session_id": "sessao_geofisico"
            }
        }
    )

    print("\nPergunta:")
    print(pergunta)

    print("\nResposta:")
    print(resposta)