from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import InventoryLoginForm
from .controller import *


def inventory_login(request):
    try:
        if request.method == 'POST':
            form = InventoryLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                res_code, res_auth = controller_validate_user_login(username=username, password=password)
                if res_code != 200:
                    form.add_error(None, res_auth)
                
                else:
                    request.session['user_id'] = res_auth['user_id']
                    request.session['user_name'] = res_auth['user_first_name'] + ' ' + res_auth['user_last_name']
                    request.session['role_id'] = res_auth['user_role_id']
                    request.session['role_name'] = res_auth['user_role_id__role_name']
                    return redirect('dashboard')
                
        else:
            form = InventoryLoginForm()

        return render(request, 'index.html', {'form': form})
    
    except Exception as ex:
        print(ex)
