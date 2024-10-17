from django.shortcuts import render
from common.utils import Authentication


@Authentication.inventory_login_decorator
def inventory_add_products(request):
    try:
        context = {}
        context['active_menu_item'] = 'Add Product'
        
        return render(request, 'inventory/view_inventory_add_products.html', context)

    except Exception as ex:
        print(ex)

@Authentication.inventory_login_decorator
def inventory_add_category(request):
    try:
        context = {}
        context['active_menu_item'] = 'Add Category'
        
        return render(request, 'inventory/view_inventory_add_category.html', context)

    except Exception as ex:
        print(ex)