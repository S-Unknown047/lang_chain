from  langchain_text_splitters import CharacterTextSplitter

doc = '''AI Overview      हिन्दी        AI semantic search is an advanced information retrieval technique t
hat understands the contextual meaning, intent, and relationships behind a user's query rather than just matc
hing exact keywords.How It WorksVector Embeddings: Machine learning models convert text,

images, or data into numerical representations called vectors and store them in a vector database.
Intent Matching: When you type a query, the system turns it into a vector and measures its proximity to 

stored data in a multi-dimensional space to find conceptual matches.Contextual Analysis: It factors in word order, 
synonyms, user location, and search history to interpret what you truly mean.Key Benefits'''

splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator='')


result = splitter.split_text(doc)

print(result)