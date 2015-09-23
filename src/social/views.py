from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from accounts.models import Player
from .forms import PostForm
import datetime

@login_required
def timeline(request):
    player = request.user
    posts = Post.objects.all()
    post_form = PostForm(player=player)
    context = {
        'player': player,
        'posts': posts,
        'post': post_form
    }

    return render(request, 'timeline.html', context)

@login_required
def post(request):
    player = Player.objects.get(pk=request.user.id)
    form = PostForm(player=player, data=request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('social:timeline')

@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        post.delete()

    return redirect('social:timeline')
