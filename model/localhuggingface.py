from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline(
    model_id="Qwen/Qwen3.8-2.4T-A95B",
    type="text-generation",
    pipeline_kwargs= dict(
        temprature=0.7,
        max_new_token=100
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("what is india")
print(result)
