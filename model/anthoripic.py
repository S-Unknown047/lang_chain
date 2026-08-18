from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-sonnet-5', temperature=1, max_tokens_to_sample=10)

result = model.invoke("what is the capital of india")

print(result.content)