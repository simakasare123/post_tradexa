from django import forms  
from employee.models import Product
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = "__all__"  