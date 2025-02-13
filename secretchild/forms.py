from django import forms

class CSVUploadForm(forms.Form):
    employees_file = forms.FileField(label="Upload Employees CSV")
    previous_file = forms.FileField(label="Upload Previous Assignments CSV", required=False)
