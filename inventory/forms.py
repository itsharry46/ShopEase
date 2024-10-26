from django import forms


class InventoryLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username', required=False)
    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not username:
            raise forms.ValidationError('Username is required.')
        
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not password:
            raise forms.ValidationError('Password is required.')
        
        return password


    
