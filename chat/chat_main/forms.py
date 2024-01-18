from django import forms
from .models import *


# форма для создания профиля
class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Member
        fields = ['avatar', 'nickname']


# форма для создания чата
class ChatForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ChatRoom
        fields = ['titles', 'participants']
