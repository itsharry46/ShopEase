from django.shortcuts import render
from common.utils import Authentication


@Authentication.inventory_login_decorator
def inventory_dashboard(request):
    try:

        context = {}
        context['active_menu_item'] = 'Dashboard'
        
        return render(request, 'inventory/view_inventory_dashboard.html', context)

    except Exception as ex:
        print(ex)
