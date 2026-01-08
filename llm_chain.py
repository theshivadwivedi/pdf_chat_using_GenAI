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

    # 3️⃣ LLM
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash",
        temperature=0
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
