from django.shortcuts import render
from common.utils import Authentication
from .models import *


@Authentication.inventory_login_decorator
def inventory_add_category(request):
    try:
        context = {}
        context['active_menu_item'] = 'Add Category'

        category_list = model_get_category_list()
        if not category_list:
            context['category_list_err'] = 'No Category Avaliable'
            return render(request, 'inventory/view_inventory_add_category.html', context)

        res_category = []
        for category_item in category_list:
            category = {}
            category['category_id'] = category_item['category_id']
            category['category_name'] = category_item['category_name']
            category['category_description'] = category_item['category_description']
            category['category_product_count'] = category_item['product_count']

            res_category.append(category)
        
        context['category_list'] = res_category
        
        return render(request, 'inventory/view_inventory_add_category.html', context)

    except Exception as ex:
        print(ex)


@Authentication.inventory_login_decorator
def inventory_add_products(request):
    try:
        context = {}
        context['active_menu_item'] = 'Add Product'
        
        return render(request, 'inventory/view_inventory_add_products.html', context)

    except Exception as ex:
        print(ex)
