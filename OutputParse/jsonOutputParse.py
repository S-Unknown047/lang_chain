from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from typing import TypedDict, Annotated, Literal, Optional
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()
# does not enfore schema
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-4-31B-it",
    task="text-generation"
)
parser = JsonOutputParser()

template1 = PromptTemplate(
    template='give me name, place, and characterstic of a fictional character\n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template1.format()
model = ChatHuggingFace(llm = llm, temprature=1.5)

# res =  model.invoke(prompt)
# final_res = parser.parse(res.content)
# print(final_res)

chain = template1 | model | parser

result = chain.invoke({})

print(result)