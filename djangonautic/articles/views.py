from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.
def article_list(request):
    article_list = Article.objects.all().order_by('date')
    context = {
        'article_list' :article_list
    }
    return render(request, "articles/article_list.html", context=context)


def article_details(request, slug):
	article = Article.objects.get(slug=slug)
	context = {'article': article}
	return render(request, 'articles/article_detail.html', context=context)
