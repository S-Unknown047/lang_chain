from langchain_community.document_loaders import TextLoader

doc = TextLoader('file.txt', encoding='utf-8')

document = doc()

print(document)