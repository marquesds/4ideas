from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import Post
from accounts.models import Player
from .forms import PostForm
import datetime


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

@login_required
def timeline(request):
    player = request.user
    players = Player.objects.all()
    posts = Post.objects.all()
    post_form = PostForm(player=player)
    context = {
        'player': player,
        'players': players,
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
