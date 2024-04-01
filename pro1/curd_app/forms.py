from django import forms
from .models import Pan


class PanForm(forms.ModelForm):
    class Meta:
        model = Pan
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(),
            "phone": forms.NumberInput(),
            "dob": forms.DateInput(),
            "marital_status": forms.RadioSelect()
        }
