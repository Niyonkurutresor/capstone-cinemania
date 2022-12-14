from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages


def registerPage(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account Has been created, Now Login! ')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'register.html', {'form':form})