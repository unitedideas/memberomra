from django import forms
from django.forms import ModelForm
from members.models import Rider
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username', 'class': "inputs_fields"}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password', 'class': "inputs_fields"}))


class AddMemberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_id', '%s')
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'placeholder': field.help_text
                })

    class Meta:
        model = Rider
        fields = '__all__'
