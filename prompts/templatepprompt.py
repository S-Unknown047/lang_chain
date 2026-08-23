from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
        template="""
            Please summarize the research paper titled "{paper}" with the following specifications:
            Explanation Style: short and with key points   
            Explanation Length: 100 words
            paper type: {paper_type}
            1. Mathematical Details:  
            - Include relevant mathematical equations if present in the paper.  
            - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
            """,
            input_variables=['paper', 'paper_type']
    )
template.save('template.json')

# to use we will use 
# from langchain_core.prompts import load_prompt
# load_prompt('filename')
