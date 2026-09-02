from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from typing import Literal
from pydantic import BaseModel, Field

load_dotenv()


class Format(BaseModel):
    feedback: Literal['positive', 'negative'] = Field(description='feedback of response')


llm = HuggingFaceEndpoint(
    repo_id="google/gemma-4-31B-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

parser = PydanticOutputParser(pydantic_object=Format)   # needs the schema
parser1 = StrOutputParser()

prompt = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {output_type}',
    input_variables=['feedback'],
    partial_variables={"output_type": parser.get_format_instructions()}   # not .output_parser()
)

prompt1 = PromptTemplate(
    template="Give an appropriate reply to this positive feedback consider this is a chat service where you are a agent don't give option give only a single professional answer: {feedback}",
    input_variables=['feedback']
)

prompt2 = PromptTemplate(
    template="Give an appropriate reply to this positive feedback consider this is a chat service where you are a agent don't give option give only a single professional answer: {feedback}",
    input_variables=['feedback']
)

chainMain = prompt | model | parser

chain = RunnableBranch(
    # convert the Format object back into a {'feedback': ...} dict
    # before it's handed to prompt1 / prompt2
    (lambda x: x.feedback == 'positive',
        RunnableLambda(lambda x: {'feedback': x.feedback}) | prompt1 | model | parser1),
    (lambda x: x.feedback == 'negative',
        RunnableLambda(lambda x: {'feedback': x.feedback}) | prompt2 | model | parser1),
    (lambda x: "could not find sentiments")
)

finalchain = chainMain | chain

result = finalchain.invoke({'feedback': 'india is a beautiful place with people belonging to different cultures, races, and colors'})  # key must be 'feedback'

print(result)