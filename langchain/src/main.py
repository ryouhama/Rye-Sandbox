from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain


def run():
    llm = ChatOpenAI(temperature=0)

    template = """Question: {question}
    Answer: """

    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "あなたの名前はなんですか？"
    answer = llm_chain.run(question)

    print(answer)


if __name__ == "__main__":
    load_dotenv()
    run()
