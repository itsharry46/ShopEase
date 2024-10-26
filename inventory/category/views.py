from .forms import *
from .models import *
from django.shortcuts import render
from common.utils import Authentication


@Authentication.inventory_login_decorator
def inventory_view_category(request):
    try:
        context = {}
        context['active_menu_item'] = 'Add Category'

        category_list = model_get_category_list()
        if not category_list:
            context['category_list_err'] = 'No Category Avaliable'
            return render(request, 'inventory/view_inventory_view_category.html', context)

        res_category = []
        for category_item in category_list:
            category = {}
            category['category_id'] = category_item['category_id']
            category['category_name'] = category_item['category_name']
            category['category_description'] = category_item['category_description']
            category['category_product_count'] = category_item['product_count']

            res_category.append(category)
        
        context['category_list'] = res_category

        # Add Category Form
        categoryForm = InventoryCreateCategoryForm()
        context['category_form'] = categoryForm

        if request.method == 'POST':
            __inventory_add_category(request)
        
        return render(request, 'inventory/view_inventory_view_category.html', context)

    except Exception as ex:
        print(ex)


def __inventory_add_category(request):
    try:

        form = InventoryCreateCategoryForm(request.POST)
        if form.is_valid():
            add_category = {}
            add_category['category_name'] = form.cleaned_data.get('category_name')
            add_category['category_description'] = form.cleaned_data.get('category_description')
            add_category['category_status'] = form.cleaned_data.get('category_status')

            res_add_category = model_add_category(add_category)
            if not res_add_category:
                raise Exception('Failed to add category into database')
            
            return res_add_category
        
    except Exception as ex:
        print(ex)
