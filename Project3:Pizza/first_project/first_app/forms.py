from django import forms
from first_app.models import Users
from django.core import validators

class NewUserform(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class loginname(forms.Form):

        Username = forms.CharField(max_length=50)
        password = forms.CharField(widget=forms.PasswordInput)

        verify_password = forms.CharField(label='Retype Password',widget=forms.PasswordInput)

        #botcatcher = forms.CharField(required = False,widget = forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


        def clean(self):
            all_clean_data = super().clean()
            password = all_clean_data['password']
            vpassword = all_clean_data['verify_password']

            if password != vpassword :
               raise forms.validationError("Make Sure Password Matches!")


        #def clean_botcatcher(self):
        #    botcatcher = self.cleaned_data['botcatcher']
        #    if len(botcatcher) > 0:
        #        raise forms.validationError("Nothing Can be done so don't try to hack XD:)!")
        #    return botcatcher
