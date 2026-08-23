from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")
chat_history = []

#//  when history go big we need to store who sent what message too this is provided by langchain
while True:
    user_input = input("you: ")
    user_input = user_input.strip().lower()
    chat_history.append(user_input)
    if user_input == 'exit': 
        break
    else:
        res = model.invoke(user_input)
        chat_history.append(res.content)
        print(f"chat: {res.content}")

