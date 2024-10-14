from django.shortcuts import render, redirect
from .models import Message, Comment, Like
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def feed_page(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(user=request.user, content=content)
        return redirect('feed:feed_page')

    messages = Message.objects.all().order_by('-created_at').prefetch_related('comment_set', 'like_set')
    return render(request, 'feed/feed.html', {'messages': messages})



@login_required
def add_comment(request, message_id):
    message = Message.objects.get(id=message_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, message=message, content=content)
        return redirect('feed:feed_page')
    
@login_required
def update_message(request, message_id):
    message = Message.objects.get(id=message_id)
    if request.user != message.user:
        return redirect('feed:feed_page')
    
    if request.method == 'POST':
        content = request.POST.get('content')
        message.content = content
        message.save()
        return redirect('feed:feed_page')
    
    return render(request, 'feed/update_message.html', {'message': message})

@login_required
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    if request.user == message.user:
        comments=Comment.objects.filter(message=message)
        for comment in comments:
            comment.delete()
        message.delete()
    return redirect('feed:feed_page')



@login_required
def like_message(request, message_id):
    message = Message.objects.get(id=message_id)
    like, created = Like.objects.get_or_create(user=request.user, message=message)
    if not created:
        like.delete()
    return redirect('feed:feed_page')

@login_required
def like_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    like, created = Like.objects.get_or_create(user=request.user, comment=comment)
    if not created:
        like.delete()
    return redirect('feed:feed_page')
