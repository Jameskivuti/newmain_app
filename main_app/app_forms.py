from django import forms

from main_app.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "dob": forms.DateInput(attrs={"min": "1990-01-01", "max": "2005-12-31", "type": "date"}),
            "kcpe_score": forms.NumberInput(attrs={"max":500, "min":0})
        }
