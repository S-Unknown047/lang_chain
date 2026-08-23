# to load chat history we first store the previous chat in the db here a text file 
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful customer support'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history=[]

with open("chatHistory.txt") as f:
  while True:
    line = f.readline()
    if not line:
      break
    chat_history.append(line)

print(chat_history)