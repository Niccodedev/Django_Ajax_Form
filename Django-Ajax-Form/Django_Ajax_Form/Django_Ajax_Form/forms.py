from django import forms

OPERATOR_CHOICES = [('sqrt','Sqrt'),('square','Square')]
class CalculationForm(forms.Form):
    operand = forms.FloatField(required = True, label = "Input the number:")
    operator = forms.ChoiceField(required = True, label="Choose operator", choices=OPERATOR_CHOICES, widget = forms.RadioSelect())
