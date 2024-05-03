from django import forms

CATEGORY_CHOICES = [
    (1, 'Food'),
    (2, 'Snacks'),
    (3, 'Drinks'),
    (4, 'Hardware'),
]

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    description = forms.CharField(widget=forms.Textarea)
    rating = forms.DecimalField(max_digits=3, decimal_places=2)