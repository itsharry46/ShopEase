from django import forms


class InventoryCreateCategoryForm(forms.Form):
    CATEGORY_STATUS_CHOICES = [
        ('Y', 'Acitve'),
        ('N', 'Inactive')
    ]

    category_name = forms.CharField(max_length=100, label='Category Name', required=False)
    category_description = forms.CharField(max_length=100, label='Category Description (Optional)', required=False)
    category_status = forms.ChoiceField(choices=CATEGORY_STATUS_CHOICES, label='Category Status', required=False)

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        print(f'-{category_name}-')
        if not category_name:
            raise forms.ValidationError('Category Name is required.')\
        
        return category_name
    
    def clean_category_description(self):
        category_description = self.cleaned_data.get('category_description')

        return category_description
    
    # def clean_category_status(self):
    #     category_status = self.cleaned_data.get('category_status')

    #     if not category_status:
    #         raise forms.ValidationError('Category Status is required.')
        
    #     return category_status
    

    