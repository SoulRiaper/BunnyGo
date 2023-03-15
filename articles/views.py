from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("my articles here")

def get_articles(request):
    return HttpResponse("""<h1>another articles here</h1> <p>and you are idiot)</p>""")

def get_one_article(request, articleNumber, articleText):
    return HttpResponse(f"""<h1>Article ID: {articleNumber}</h1> <p>Article text: {articleText}</p>""")

def get_article_as_json(req):
    return JsonResponse({"number" : 13, "text": "Jopa popa syela trusi"})