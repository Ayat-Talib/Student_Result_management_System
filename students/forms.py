from django import forms
from .models import Student, Result

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'email', 'class_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['subject', 'marks_obtained']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'marks_obtained': forms.NumberInput(attrs={'class': 'form-control'}),
        }