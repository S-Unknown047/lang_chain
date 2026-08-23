from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# SystemMessage (is the initaial message sent such as act as a doctor etc), AIMessage (msg sent by ai), HumanMessage (sent by user)
model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

message = []

SystemMessage(content="be a helpful assistant")
# this is the another method
chat_history = ChatPromptTemplate([
    ('system', "you are a helpful {domain} expert"),
    ('human', 'explain in simple terms what is {topic}')
])


prompt = chat_history.invoke({'domain':'python', 'topic':'object in python'})



while True:
    user_input = input("you: ")
    user_input = user_input.strip().lower()
    message.append(HumanMessage(content=user_input))
    if user_input == 'exit': 
        break
    else:
        res = model.invoke(message)
        
        message.append(AIMessage(content=(res.text)))
        print(f"chat: {res.text}")

print(message)