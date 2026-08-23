from django.http import HttpResponse

def homepage(request):
    return HttpResponse('this is home page')

