from django import forms
from django.core import validators

def gmail_verifications(value):
    if value[len(value)-9:]!='gmail.com':
        raise forms.ValidationError('must be gmail')
class studentRegistration(forms.Form):
    name=forms.CharField()
    roll=forms.IntegerField()
    email=forms.EmailField(validators=[gmail_verifications])
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea, validators=[validators.MinLengthValidator(10),validators.MaxLengthValidator(20)])

    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError('length of name field should be>=4')
        return inputname

    def clean_roll(self):
        inputroll=self.cleaned_data['roll']
        if inputroll<10:
            raise forms.ValidationError('roll field should be>=10')
        return inputroll

    def clean(self):
        print('total form varifcation')
        cleaned_data=super().clean()
        inputpwd1=cleaned_data['password']
        inputpwd2=cleaned_data['rpassword']
        if inputpwd1!=inputpwd2:
                raise forms.ValidationError('password not matched')
