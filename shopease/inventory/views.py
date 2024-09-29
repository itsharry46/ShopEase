from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import *
from .models import *
import hashlib


def inventory_login(request):
    try:
        if request.method == 'POST':
            form = InventoryLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                password = hashlib.md5(password.encode()).hexdigest()
                res_user_details = model_get_user_details(username, password)
                if not res_user_details:
                    form.add_error(None, "Invalid login credentials")
                
                else:
                    request.session['user_logged_in'] = True
                    request.session['user_id'] = res_user_details['user_id']
                    request.session['user_name'] = res_user_details['user_first_name'] + ' ' + res_user_details['user_last_name']
                    request.session['role_id'] = res_user_details['user_role_id']
                    request.session['role_name'] = res_user_details['user_role_id__role_name']
                    return redirect('dashboard')
                
        else:
            form = InventoryLoginForm()

        return render(request, 'index.html', {'form': form})
    
    except Exception as ex:
        print(ex)


def inventory_logout(request):
    try:
        logout(request)
        return redirect('inventory_login')

    except Exception as ex:
        print(ex)