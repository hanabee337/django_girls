from django import forms


# templates의 form안에 있는 field들을 자동으로 만들어 주는 역할을 한다.
class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(
        widget=forms.Textarea
    )
