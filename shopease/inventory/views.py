from django.shortcuts import render, redirect, HttpResponse
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
                    user_full_name = res_user_details['user_first_name'] + ' ' + res_user_details['user_last_name']

                    request.session['user_logged_in'] = True
                    request.session['user_id'] = res_user_details['user_id']
                    request.session['user_name'] = user_full_name
                    request.session['user_initial'] = f'{user_full_name[0][0].capitalize()}{user_full_name[1][0].capitalize()}'
                    request.session['role_id'] = res_user_details['user_role_id']
                    request.session['role_name'] = res_user_details['user_role_id__role_name']

                    # Added user access control
                    user_artifacts = []
                    res_user_artifacts = model_get_user_artifacts(res_user_details['user_role_id'])

                    for artifacts in res_user_artifacts:
                        
                        sub_module = {}
                        sub_module['sub_module_id'] = artifacts['submodule__sub_module_id']
                        sub_module['sub_module_name'] = artifacts['submodule__sub_module_name']
                        sub_module['sub_module_link'] = artifacts['submodule__sub_module_link']
                        sub_module['sub_module_create_status'] = artifacts['submodule__artifact__artifact_create_status']
                        sub_module['sub_module_read_status'] = artifacts['submodule__artifact__artifact_read_status']
                        sub_module['sub_module_update_status'] = artifacts['submodule__artifact__artifact_update_status']
                        sub_module['sub_module_delete_status'] = artifacts['submodule__artifact__artifact_delete_status']

                        module_index = next((i for i, item in enumerate(user_artifacts) if ( 'module_id' in item ) and (item["module_id"] == artifacts['module_id']) ), None)
                        if module_index is None:
                            module = {}
                            module['module_id'] = artifacts['module_id']
                            module['module_name'] = artifacts['module_name']
                            module['sub_module'] = []

                            user_artifacts.append(module)

                        if len(user_artifacts) == 1:
                            user_artifacts[0]['sub_module'].append(sub_module)
                        elif module_index is None:
                            module_index = len(user_artifacts)
                            user_artifacts[int(module_index) - 1]['sub_module'].append(sub_module)
                        else:
                            user_artifacts[module_index]['sub_module'].append(sub_module)

                    request.session['user_artifacts'] = user_artifacts

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

