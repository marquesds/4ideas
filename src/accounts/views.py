from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

def join(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        user = authenticate(
            username=user.username,
            password=form.cleaned_data['password1']
        )
        login(request, user)
        return redirect('social:timeline')

    context = {
        'form': form
    }

    return render(request, 'join-us.html', context)
