from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embed = OpenAIEmbeddings(model="", dimensions=40)


result = embed.embed_query("delhi is capital")

#embedding documents

# embed.embed_documents()
print(str(result))