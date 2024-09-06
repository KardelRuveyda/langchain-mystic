from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage
from typing import Any
import os

load_dotenv()

embeddings= AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    openai_api_version=os.getenv("OPENAI_API_VERSION")
)

llm = AzureChatOpenAI(
    deployment_name= os.getenv("DEPLOYMENT_NAME"),
    temperature=0.2,
)

vector=FAISS.load_local(
    "./vectors/mystic",embeddings,allow_dangerous_deserialization=True
)

retriever = vector.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k":2,"score_threshold":0.7},
)


def get_response(query: str) -> Any:
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Sen bir rüya tabirleri botusun,sana gönderdiğim dosyalardan en uygun cevapları göndermen gerekiyor."
            ),
            (
                "user",
                """\
                ###
                Context:\
                {context}
                RULES:
                1- Sadece gönderdiğimiz dosyalardan cevaplaman gerekiyor.
                2- Gönderdiğimiz contextleri incele 

                kullanıcının sordupu soru:\                                    
                {input}
                """
                
            )
        ]
    )
    
    document_chain=create_stuff_documents_chain(llm,prompt)

    retriever_chain=create_retrieval_chain(retriever,document_chain)

    response= retriever_chain.invoke({"input": query})

    return response

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]
    st.session_state.history=[]

st.set_page_config(page_title="Mystic Bot🔮")

st.title("Mystic Bot🔮")

user_query= st.chat_input("yazınız")

for messages in st.session_state.chat_history:
    if isinstance (messages,HumanMessage):
        with st.chat_message("Human"):
            st.markdown(messages.content)
    else:
        with st.chat_message("AI"):
            st.markdown(messages.content)

if user_query is not None and user_query!="":
    st.session_state.chat_history.append(HumanMessage(user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        result=get_response(user_query)
        st.markdown(result)
        st.markdown(result["answer"])
        st.session_state.chat_history.append(AIMessage(result["answer"]))
