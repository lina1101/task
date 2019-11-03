from django import forms


class FibonacciForm(forms.Form):
    n = forms.IntegerField(min_value=0)


class AckermannForm(forms.Form):
    m = forms.IntegerField(min_value=0)
    n = forms.IntegerField(min_value=0)


class FactorialForm(forms.Form):
    n = forms.IntegerField(min_value=0)
