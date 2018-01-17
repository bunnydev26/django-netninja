from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup_view(request):
	context = {}
	if request.method == 'POST':
		# We Basically load the data from the post request to the signup_form
		signup_form = UserCreationForm(request.POST)
		# Check if the username & Password match passes all the required validation.
		if signup_form.is_valid():
			# Save the form.
			signup_form.save()
			# Log the user in.
			return redirect('articles:list')
		else:
			context['signup_form'] = signup_form	
	else:
		signup_form = UserCreationForm()
		context['signup_form'] = signup_form
		
	return render(request, "accounts/signup.html", context=context)

def login_view(request):
	context = {}
	if request.method == 'POST':
		login_form = AuthenticationForm(data=request.POST)
		context['login_form'] = login_form
		if login_form.is_valid():
			# Login the user
			user = login_form.get_user()
			login(request, user)
			return redirect("articles:list")
	else:
		login_form = AuthenticationForm()
		context['login_form'] = login_form

	return render(request, "accounts/login.html", context=context)

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect("articles:list")