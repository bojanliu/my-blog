#-*-coding:utf-8-*-
from django import forms
from captcha.fields import CaptchaField

class contactform(forms.Form):
    subject=forms.CharField(max_length=50,label=('主题（必填）'))
    email=forms.EmailField(label=('邮箱（必填，不公开）'))
    message=forms.CharField(widget=forms.Textarea(),label=('内容（必填）'))
    captcha=CaptchaField(label=('验证码（必填）'))

    def clean_message(self):
        message=self.cleaned_data.get('message','')
        num_words=len(message.split())
        if num_words < 4:
            raise forms.ValidationError('Not enough words!')
        return message

