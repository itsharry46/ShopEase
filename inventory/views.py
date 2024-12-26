import hashlib
from .forms import *
from .models import *
from common.utils import CustomLogging
from django.shortcuts import render, redirect

# Logger details
logger = CustomLogging.setup_logger(__name__)


def inventory_login(request):
    try:
        if request.method == 'POST':
            
            form = InventoryLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
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
                        module = {}
                        module['module_id'] = artifacts['artifact_module_id__module_id']
                        module['module_name'] = artifacts['artifact_module_id__module_name']
                        module['module_icon'] = artifacts['artifact_module_id__module_icon']
                        module['module_link'] = artifacts['artifact_module_id__module_link']
                        module['module_create_status'] = artifacts['artifact_create_status']
                        module['module_read_status'] = artifacts['artifact_read_status']
                        module['module_update_status'] = artifacts['artifact_update_status']
                        module['module_delete_status'] = artifacts['artifact_delete_status']

                        user_artifacts.append(module)
                    
                    request.session['user_artifacts'] = user_artifacts

                    return redirect('inventory_dashboard')
                
        else:
            form = InventoryLoginForm()

        return render(request, 'inventory/view_inventory_login.html', {'form': form})

    except Exception as ex:
        logger.error(ex)


def inventory_logout(request):
    try:
        request.session.flush()
        return redirect('inventory_login')
    
    except Exception as ex:
        logger.error(ex)

