from django import forms
from .models import Job, Apply

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'desc', 'long_desc']

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply 
        fields = ['content', 'experience']
