from django import forms

class ViewPassword(forms.Form):
    accname = forms.CharField(label="Account Name", max_length=100)

class CreatePassword(forms.Form):
    name = forms.CharField(label="Account Name", max_length=100)
    length = forms.IntegerField(min_value=8, max_value=18)

class DeletePassword(forms.Form):
    delaccname = forms.CharField(label="Account Name", max_length=100)

class ModifyPassword(forms.Form):
    modifaccname = forms.CharField(label="Account Name", max_length=100)
    new_length = forms.IntegerField(min_value=8, max_value=18)
