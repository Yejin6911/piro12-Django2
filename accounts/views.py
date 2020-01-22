from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import CreateView
from .forms import SignupForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save() #회원가입 완료된 상황
#             #로그인 처리
#             auth_login(request, user)
#             return redirect('profile')
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {
#         'form' : form,
#     })

#클래스 기반 - CreateView 상속받아 이용
class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile') #문자로 날려주어야 하기 때문에 redirect 함수 대신 사용용

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()


##클래스 기반
# signup = CreateView.as_view(model=User,
#                             form_class=SignupForm,
#                             success_url=settings.LOGIN_URL,
#                             template_name='accounts/signup.html')

@login_required
def profile(request): #setting.LOGIN_URL로 로그아웃일때는 이동
    #request.user #django.contrib.auth.models.User(로그인되어있을 때) 또는 django.contrib.auth.models.AnonymousUser(로그인 X일 때)
    return render(request, 'accounts/profile.html')


