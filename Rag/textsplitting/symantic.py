from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings


# Initialize your embedding model
embedd = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"

)

doc = '''The exploration of deep space remains one of humanity's greatest scientific ambitions. Engineers and astronomers work tirelessly to design advanced rovers and telescopes capable of detecting biosignatures on distant planets. Mars has been a primary focus, with missions aiming to uncover evidence of ancient microbial life beneath its arid, radiation-swept surface. Rocket propulsion technologies are also evolving, paving the way for faster transit times across the solar system.

To achieve the perfect texture in sourdough baking, maintaining a stable temperature during fermentation is absolutely critical. Bakers often monitor the ambient room environment and adjust their hydration levels to control how quickly the wild yeast consumes available sugars. A long, cold proof in the refrigerator helps develop complex lactic acids, resulting in that signature tangy flavor and a beautifully blistered crust.

Managing your personal finances effectively requires a disciplined approach to both budgeting and long-term investing. Financial advisors frequently emphasize the power of compound interest, which allows small, consistent contributions to grow exponentially over several decades. Diversifying your portfolio across low-cost index funds and bonds helps mitigate market volatility and safeguards your savings against unexpected economic downturns.
'''

# Create the semantic chunker
text_splitter = SemanticChunker(embedd, breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3)

# Split your document or raw text
docs = text_splitter.split_text(doc)

print(docs)
