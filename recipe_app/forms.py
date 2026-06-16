from django import forms


class RecipeForm(forms.Form):

    ingredients = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "placeholder": "Enter ingredients..."
            }
        )
    )

    image = forms.ImageField(
        required=False
    )