from django import forms


class InventoryProductFilterForm(forms.Form):
    
    product_status = forms.CharField(max_length=100, label='Product Status', required=False)
    product_category = forms.CharField(max_length=100, label='Product Category', required=False)
    

    