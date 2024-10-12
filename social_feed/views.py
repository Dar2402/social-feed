from django.shortcuts import render, redirect


def redirection(request):
    if request.user.is_authenticated:
        return redirect('feed:feed_page')
    else:
        return redirect('accounts:login')

