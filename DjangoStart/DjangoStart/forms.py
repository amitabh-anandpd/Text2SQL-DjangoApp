from Django import forms

class codeInput(forms.Form):
    code = forms.CharField()
    code.widget.attrs.update({'placeholder': 'Enter Monitor code'})