from django import forms


class CourseForm(forms.Form):
    name = forms.CharField(label="Name")
    subtitle = forms.CharField(required=False)
    image = forms.FileField()
    price = forms.CharField(required=False)
