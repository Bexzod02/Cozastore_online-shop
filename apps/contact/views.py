from django.shortcuts import render, redirect

# Create your views here.
from .forms import CreateContactForm
# Create your views here.


def contact(request):
    form = CreateContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    ctx = {
        'form':form,
    }
    return render(request, 'contact.html', ctx)

def about(request):
    return render(request, 'about.html')