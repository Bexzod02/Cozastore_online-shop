from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from apps.account.forms import SingUpForm
# Create your views here.

def registration_view(request):
    # context = {}
    # if request.POST:
    #     form = SingUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         email = form.cleaned_data.get('email')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = form.save()
    #         account = authenticate(email=email, password=raw_password)
    #         login(request, user)
    #         return redirect('login')
    #     else:
    #         context['form'] = form

    # else:
    #     form = SingUpForm()
    #     context['form'] = form
    return render(request, 'login.html')