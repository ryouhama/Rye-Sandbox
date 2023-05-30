from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


def run():
    llm = ChatOpenAI(temperature=0)
    memory = ConversationBufferMemory(return_messages=True)

    template = "以下は、人間とAIの友好的な会話です。AIは人間の発言を理解し、それに対して適切な返答をします。"

    # テンプレートを用いてプロンプトを作成
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(template),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}")
    ])
    conversation = ConversationChain(llm=llm, memory=memory, prompt=prompt)

    command = input("😇 : ")

    while True:
        response = conversation.predict(input=command)
        print(f"🤖 : {response}")
        command = input("😇 : ")
        if command == "exit":
            break


if __name__ == "__main__":
    load_dotenv()
    run()
