from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            'first_name': 'Your first name',
            'last_name': 'Your last name',
            'starts': 'Your rating',
        }
        error_messages = {
            'starts': {
                'max_value': "Your max value es 5",
                'min_value': "Your min value es 1",
            }
        }

  