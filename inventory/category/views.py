import json
from .forms import *
from .models import *
from django.shortcuts import render
from django.http import JsonResponse
from common.utils import Authentication, CustomLogging, Cryptography

# Logger details
logger = CustomLogging.setup_logger(__name__)


@Authentication.inventory_login_decorator
def inventory_view_category(request):
    try:
        context = {}
        context['active_menu_item'] = 'Add Category'

        # Add Category Form
        categoryForm = InventoryCreateCategoryForm()
        context['category_form'] = categoryForm
        context['category_form_status'] = False

        return render(request, 'inventory/view_inventory_view_category.html', context)

    except Exception as ex:
        logger.error(ex)


@Authentication.inventory_login_decorator
def inventory_view_category_fetch(request):
    try:
        if request.method == 'GET':
            # Params Code
            query_params = request.GET.get('query_params', None)
            if not query_params:
                err_msg = 'Some issue in query params of inventory_view_category_fetch'
                logger.error(err_msg)
                
                res_error = {}
                res_error['message'] = err_msg
                
                return JsonResponse(res_error, status=400)
            
            query_params = Cryptography.query_param_decryption(query_params)

            filters = {}
            filters['search_category'] = query_params.get('search_category', [None])[0]

            
            result = {}
            category_list = model_get_category_list(filters)
            if not category_list:
                return JsonResponse({}, status=200)
            
            res_category = []
            for category_item in category_list:
                category = {}
                category['category_id'] = category_item['category_id']
                category['category_name'] = category_item['category_name']
                category['category_description'] = category_item['category_description']
                category['category_product_count'] = category_item['product_count']
                category['category_status'] = category_item['category_status']

                res_category.append(category)
            
            result['category_list'] = res_category

            return JsonResponse(result, status=200)
        

        res_error = {}
        res_error['message'] = 'Wrong method has been envoked'
        
        return JsonResponse(res_error, status=400)

    except Exception as ex:
        logger.error(ex)


@Authentication.inventory_login_decorator
def inventory_add_category(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)

            categoryForm = InventoryCreateCategoryForm(body)
            if categoryForm.is_valid():
                add_category = {}
                add_category['category_name'] = categoryForm.cleaned_data.get('category_name')
                add_category['category_description'] = categoryForm.cleaned_data.get('category_description')
                add_category['category_status'] = categoryForm.cleaned_data.get('category_status')

                res_add_category = model_add_category(add_category)
                if not res_add_category:
                    raise Exception('Failed to add category into database')
                
                result = {}
                result['message'] = 'Category Created Successfully!'

                return JsonResponse(result, status=200)
            
            else:
                return JsonResponse(categoryForm.errors, status=400)


    except Exception as ex:
        logger.error(ex)


@Authentication.inventory_login_decorator
def inventory_info_update_category(request):
    try:
        if request.method == 'GET':
            category_id = request.GET.get('category_id')
            if not category_id:
                raise Exception('Please connect with developer')
            
            res_info_category = model_update_category_information(category_id)
            if not res_info_category:
                raise Exception('Failed to fetch category information')
            
            result = {}
            result['category_name'] = res_info_category[0]['category_name']
            result['category_description'] = res_info_category[0]['category_description']
            result['category_status'] = res_info_category[0]['category_status']

            return JsonResponse(result, status=200)

    except Exception as ex:
        logger.error(ex)
        

@Authentication.inventory_login_decorator
def inventory_update_category(request):
    try:
        if request.method == 'PUT':
            body = json.loads(request.body)

            categoryForm = InventoryCreateCategoryForm(body)
            if categoryForm.is_valid():
                category_id = body.get('category_id')
                if not category_id:
                    raise Exception('Category ID is not present')

                update_category = {}
                update_category['category_name'] = categoryForm.cleaned_data.get('category_name')
                update_category['category_description'] = categoryForm.cleaned_data.get('category_description')
                update_category['category_status'] = categoryForm.cleaned_data.get('category_status')

                res_update_category = model_update_category(category_id, update_category)
                if not res_update_category:
                    raise Exception('Failed to update category into database')
                
                result = {}
                result['message'] = 'Category Updated Successfully!'

                return JsonResponse(result, status=200)

            else:
                return JsonResponse(categoryForm.errors, status=400)


    except Exception as ex:
        logger.error(ex)


@Authentication.inventory_login_decorator
def inventory_delete_category(request):
    try:
        if request.method == 'DELETE':
            category_id = request.GET.get('category_id')
            if not category_id:
                raise Exception('Category ID is not present')

            res_delete_category = model_delete_category(category_id)
            if not res_delete_category:
                raise Exception('Failed to delete category into database')

            result = {}
            result['message'] = 'Category Deleted Successfully!'

            return JsonResponse(result, status=200)
        

    except Exception as ex:
        logger.error(ex)