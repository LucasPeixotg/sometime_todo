from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    task_title = forms.CharField(label='Task',)
    task_description = forms.CharField(
        label='Description', 
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'materialize-textarea',
                'rows': 10,
                'cols': 30,
            }
        ))

    class Meta:
        model = Task
        fields = [
            'task_title',
            'task_description',
        ]
    
