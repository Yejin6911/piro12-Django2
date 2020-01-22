from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import SignupForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm()
#         if form.is_valid():
#             user = form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {
#         'form' : form,
#     })

#클래스 기반
signup = CreateView.as_view(model=User,
                            form_class=SignupForm,
                            success_url=settings.LOGIN_URL,
                            template_name='accounts/signup.html')

CreateView
@login_required
def profile(request): #setting.LOGIN_URL로 로그아웃일때는 이동
    #request.user #django.contrib.auth.models.User(로그인되어있을 때) 또는 django.contrib.auth.models.AnonymousUser(로그인 X일 때)
    return render(request, 'accounts/profile.html')


