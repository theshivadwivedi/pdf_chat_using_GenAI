from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def build_chain(vectorstore):
    # 1️⃣ Retriever
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    # 2️⃣ Prompt
    prompt = ChatPromptTemplate.from_template(
        """
        Use the following context to answer the question.
        If the answer is not in the context, say "I don't know".

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

from config import get_google_api_key

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=get_google_api_key()
)

    # 4️⃣ LCEL Chain
chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
)
return chain
