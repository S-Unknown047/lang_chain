from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
import os 
import json

load_dotenv()

@csrf_exempt
def summaryGenerator(request):
    if request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)
    
    key = os.getenv('HUGGINGFACEHUB_API_TOKEN')
    print(f"{key}")
    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        data = {}

    paper_type= data.get('paperType')
    paper = data.get('paper')

    print(f"paper {paper_type} {paper}")
    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen3.8-2.4T-A95B",
        task="text-generation"
    )   

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

    model = ChatHuggingFace(llm = llm)
  # Create plain string prompt
    prompt_text = template.format(paper=paper, paper_type=paper_type)

    print("Formatted Prompt:", prompt_text)

    res = model.invoke(prompt_text)
    print("Model Response:", res.content)
    summary = res.content
    print(f"{summary}")
    resp = JsonResponse({'summary': summary})
    resp['Access-Control-Allow-Origin'] = '*'
    return resp



