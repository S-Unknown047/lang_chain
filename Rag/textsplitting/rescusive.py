from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

doc = '''AI Overview      हिन्दी        AI semantic search is an advanced information retrieval technique t
hat understands the contextual meaning, intent, and relationships behind a user's query rather than just matc
hing exact keywords.How It WorksVector Embeddings: Machine learning models convert text,

images, or data into numerical representations called vectors and store them in a vector database.
Intent Matching: When you type a query, the system turns it into a vector and measures its proximity to 

stored data in a multi-dimensional space to find conceptual matches.Contextual Analysis: It factors in word order, 
synonyms, user location, and search history to interpret what you truly mean.Key Benefits'''

# it work such that at a first divide based of para (if chuk size seh kam para len then no issue) then if jyada hai then go for para then words then character
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=0)
splitter = RecursiveCharacterTextSplitter(language= Language.PYTHON, chunk_size=300, chunk_overlap=0)
res = splitter.split_text(doc)

print(len(res))

print(res)
doc = '''AI Overview      हिन्दी        AI semantic search is an advanced information retrieval technique t
hat understands the contextual meaning, intent, and relationships behind a user's query rather than just matc
hing exact keywords.How It WorksVector Embeddings: Machine learning models convert text,

images, or data into numerical representations called vectors and store them in a vector database.
Intent Matching: When you type a query, the system turns it into a vector and measures its proximity to 

stored data in a multi-dimensional space to find conceptual matches.Contextual Analysis: It factors in word order, 
synonyms, user location, and search history to interpret what you truly mean.Key Benefits'''