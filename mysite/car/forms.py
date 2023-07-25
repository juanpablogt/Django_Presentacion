from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='Your first name', max_length=100)
    last_name = forms.CharField(label='Your last name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)
    review = forms.CharField(label = 'please write your review', widget=forms.Textarea(attrs={'class':'myform'}))#desde aqui se puede controlar la linea punteada que aparece en el campo de mensaje

