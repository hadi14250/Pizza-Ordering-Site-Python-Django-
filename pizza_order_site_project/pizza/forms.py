from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     toppings = forms.MultipleChoiceField(choices=[("pep", "Pepperoni"), ("cheese", "Cheese"), ("olives", "Olives")])
#     # we have two names here in the choces list because there is a visual name and the actual name
#     size = forms.ChoiceField(label="Size", choices=[("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")])


class PizzaForm(forms.ModelForm):


    # image = forms.ImageField()

    class Meta:
        model = Pizza
        fields = ["topping1", "topping2", "size"]
        labels = {"topping1": "Topping 1", "topping2": "Topping 2"}


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=10)