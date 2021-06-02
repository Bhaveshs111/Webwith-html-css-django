from django import forms

class New_book_form(forms.Form):
    dpt = forms.CharField( label="department:" )
    title=forms.CharField(label="Title:",max_length=50)
    author=forms.CharField(label="Author:",max_length=25)
    pbr=forms.CharField(label="Publisher:",max_length=25)
    price = forms.FloatField( label="price:" )

class Search_form_T(forms.Form):
    title=forms.CharField(label="Title:", max_length=50)
class Search_form_D(forms.Form):
    dpt=forms.CharField(label="Department:", max_length=50)
class Search_form_P(forms.Form):
    pbr=forms.CharField(label="Publisher:", max_length=50)
class Search_form_A(forms.Form):
    author=forms.CharField(label="Author", max_length=50)