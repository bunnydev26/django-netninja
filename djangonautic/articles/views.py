from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
# The following is a decorator which is used to protect 
# the view from executing if the user is not authenticated
from django.contrib.auth.decorators import login_required
from .forms import CreateArticles

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

@login_required(login_url='/accounts/login/')
def article_create(request):
	context = {}
	
	article_forms = None
	if request.method == 'POST':
		article_forms = CreateArticles(data=request.POST, files=request.FILES)
		if article_forms.is_valid():
			article_instance = article_forms.save(commit=False)
			article_instance.author = request.user
			article_instance.save()
			return redirect("articles:list")
	else:
		article_forms = CreateArticles()

	context['article_forms'] = article_forms
	return render(request, 'articles/article_create.html', context=context)