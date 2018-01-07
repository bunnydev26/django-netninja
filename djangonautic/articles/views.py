from django.shortcuts import render
from .models import Article
# Create your views here.
def article_list(request):
    article_list = Article.objects.all().order_by('date')
    context = {
        'article_list' :article_list
    }
    return render(request, "articles/article_list.html", context=context)
