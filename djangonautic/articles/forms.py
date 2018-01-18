from django import forms
from .models import Article

class CreateArticles(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'body', 'slug', 'thumb']