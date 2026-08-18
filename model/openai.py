from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
# temperature controls the randomness and creativity of the model's responses.

# For OpenAI models, the value typically ranges from 0.0 to 2.0.
# How it affects the output

#     Low Temperature (0.0 – 0.3): Focused & Deterministic

#         The model almost always picks the most mathematically probable next word.

#         Outputs are predictable, factual, and consistent.

#         Best for: Coding, math, JSON formatting, factual Q&A.

#     Moderate Temperature (0.7 – 1.0): Balanced

#         Provides a balance between coherent structure and natural conversational variety.

#         Best for: General conversation, blog writing, email drafting.

#     High Temperature (1.2 – 2.0, such as your 1.5): Highly Creative & Random

#         The probability distribution flattens, giving less common words a higher chance of being chosen.

#         Outputs become more diverse, unexpected, and imaginative, but also carry a higher risk of hallucinations, typos, or nonsensical phrasing.

#         Best for: Brainstorming novel ideas, poetry, creative fiction.


# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage

# llm = ChatOpenAI(model="gpt-4o")

# message = HumanMessage(
#     content=[
#         {"type": "text", "text": "Describe this image"},
#         {
#             "type": "image_url",
#             "image_url": {
#                 "url": "https://example.com/image.jpg"
#             }
#         }
#     ]
# )

# response = llm.invoke([message])
# print(response.content)

# import base64

# with open("image.jpg", "rb") as f:
#     image_b64 = base64.b64encode(f.read()).decode()

# message = HumanMessage(
#     content=[
#         {"type": "text", "text": "What is in this image?"},
#         {
#             "type": "image_url",
#             "image_url": {
#                 "url": f"data:image/jpeg;base64,{image_b64}"
#             }
#         }
#     ]
# )
# import base64
# from langchain_core.messages import HumanMessage

# with open("speech.wav", "rb") as f:
#     audio_b64 = base64.b64encode(f.read()).decode()

# message = HumanMessage(
#     content=[
#         {"type": "text", "text": "Transcribe this audio"},
#         {
#             "type": "input_audio",
#             "input_audio": {
#                 "data": audio_b64,
#                 "format": "wav"
#             }
#         }
#     ]
# )

load_dotenv()



model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("write a poem")

print(result.content)