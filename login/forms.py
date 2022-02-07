from django import forms 
from .models import Student
from .models import School

class StudentForm(forms.ModelForm): 
    class Meta:
        model= Student
        fields= '__all__' 

class SchoolForm(forms.ModelForm):
    class Meta :
        model = School
        fields = '__all__' 
 
