from django import forms

CATEGORY_CHOICES = [(1, 'Food'), (2, 'Snack'), (3, 'Drinks'), (4, 'Hardware')]
class ProductForm(forms.Form):
    product_name=forms.CharField(max_length=1000)
    category=forms.ChoiceField(choices=CATEGORY_CHOICES)
    description=forms.ChoiceField(widget=forms.Textarea)
    rating=forms.IntegerField(min_value=1, max_value=5)
