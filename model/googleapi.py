import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# api_key = os.getenv("API")
# print(f"api_key is {api_key}")

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")
result = model.invoke("What is the capital of India?")
print(result.text)
