from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request): #setting.LOGIN_URL로 로그아웃일때는 이동
    #request.user #django.contrib.auth.models.User(로그인되어있을 때) 또는 django.contrib.auth.models.AnonymousUser(로그인 X일 때)
    return render(request, 'accounts/profile.html')
