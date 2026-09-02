from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="Generate a detail report on {topic}",
    input_variables= ['topic']
)

promptS = PromptTemplate(
    template="Give a summary in 5 lines {text}",
    input_variables= ['text']
)

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-4-31B-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt | model | parser | model | parser

result = chain.invoke ({'topic':'unemployment in india'})

print(result)

