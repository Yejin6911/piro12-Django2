from django.contrib.auth.forms import UserCreationForm

#추가적인 필드에 대해서만 추가적으로 구현해 주면 됌
class SignupForm(UserCreationForm):
    pass