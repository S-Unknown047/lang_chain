from  pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-4-31B-it",
    task="text-generation"
)

class Person(BaseModel):
    name: str = Field(description='NAME OF THE PERSON')
    age: int = Field(description="age of the person")
    city: str = Field(gt = 18, description='Name of the city')



parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate name, age and city of a fictional {place} character.\n{format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

model = ChatHuggingFace(llm=llm)
prompt = template.invoke({'place':'india'})

res = model.invoke(prompt)

final_res = parser.parse(res.content)
print(final_res)