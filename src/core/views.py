from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Player

@login_required
def index(request):
    player = request.user
    context = {
        'player': player
    }
    return render(request, 'timeline.html', context)
