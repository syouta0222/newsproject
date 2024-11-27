from django.forms import ModelForm
from .models import ArticlePost

class ArticlePostForm(ModelForm):

    class Meta:
        model = ArticlePost
        fields = ['category', 'title', 'article', 'image1', 'image2']


from django import forms

# 入力確認を行うクラスを作成
class ContactForm(forms.Form):
    # HTML側のデータを取得
    name = forms.CharField(label='お名前')
    email=forms.CharField(label='メールアドレス')
    title=forms.CharField(label='件名')
    message=forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'

