from django import forms

class InputForm(forms.Form):
    nlInput = forms.CharField()
    nlInput.widget.attrs.update({'placeholder': 'Enter Natural Language Query'})

class SQLFileUploadForm(forms.Form):
    sql_file = forms.FileField(label='Upload SQL Database')