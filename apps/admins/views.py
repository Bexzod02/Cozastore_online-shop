from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate



def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    return render(request, 'login.html', {'form': form})


def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect('/admins/')

    return render(request, 'logout.html', {})


from apps.admins.forms import SingUpForm


def registration_view(request):
    context = {}
    if request.POST:
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            user = form.save()
            # account = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('login')
        else:
            context['form'] = form

    else:
        form = SingUpForm()
        context['form'] = form
    return render(request, 'register.html', context)

