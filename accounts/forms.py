from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
#추가적인 필드에 대해서만 추가적으로 구현해 주면 됌
class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = 'Enter email format'
        self.fields['username'].label = 'Email'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.username
        if commit:
            user.save()
        return user
    # def clean_username(self):
    #     value = self.cleaned_data_get('username')
    #     #각 필드에 대한 validators, clean_필드명, clean등을 사용
    #     if value:
    #         validate_email(value)