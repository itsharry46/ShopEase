import math
from .forms import *
from .models import *
from django.shortcuts import render
from django.http import JsonResponse
from common.utils import Authentication, CustomLogging, Cryptography
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Logger details
logger = CustomLogging.setup_logger(__name__)


@Authentication.inventory_login_decorator
def inventory_view_products(request):
    try:
        if request.method == 'GET':
            
            context = {}
            context['active_menu_item'] = 'Product Listing'

            category_list = model_get_category_list()
            res_category = []
            res_category.append({'category_id': None, 'category_name': 'Select Product Category'})
            for category_item in category_list:
                category = {}
                category['category_id'] = category_item['category_id']
                category['category_name'] = category_item['category_name']

                res_category.append(category)

            
            context['category_list'] = res_category

            category_status = []
            category_status.append({'category_status_id': None, 'category_status': 'Select Category Status'})
            category_status.append({'category_status_id': 'Y', 'category_status': 'Active'})
            category_status.append({'category_status_id': 'N', 'category_status': 'Inactive'})
            context['category_status'] = category_status

            category_stock = []
            category_stock.append({'stock_id': None, 'stock_status': 'Select Product Stock Status'})
            category_stock.append({'stock_id': 'Y', 'stock_status': 'In Stock'})
            category_stock.append({'stock_id': 'N', 'stock_status': 'Out Of Stock'})
            context['category_stock_status'] = category_stock

            return render(request, 'inventory/view_inventory_view_products.html', context)
        
        res_error = {}
        res_error['message'] = 'This request is not allowed'
        return JsonResponse(res_error, status=400)

    except Exception as ex:
        logger.error(ex)


@Authentication.inventory_login_decorator
def inventory_view_products_fetch(request):
    try:
        if request.method == 'GET':
            # Params Code
            query_params = request.GET.get('query_params', None)
            if not query_params:
                err_msg = 'Some issue in query params of inventory_view_products_fetch'
                logger.error(err_msg)
                
                res_error = {}
                res_error['message'] = err_msg
                
                return JsonResponse(res_error, status=400)

            query_params = Cryptography.query_param_decryption(query_params)
            
            page_number = query_params.get('page', [1])[0]

            filters = {}
            filters['category_status'] = query_params.get('category_status')[0]
            filters['product_category'] = query_params.get('product_category')[0]
            filters['product_stock_status'] = query_params.get('product_stock_status')[0]
            filters['search_product'] = query_params.get('search_product', [None])[0]

            # Pagination Code
            per_page = 10
            offset = (int(page_number) - 1) * per_page
            limit = offset + per_page

            result = {}

            product_list = model_get_product_list(offset, limit, filters)
            res_products = []
            for items in product_list['data_item']:
                product = {}
                product['product_id'] = items['product_id']
                product['product_name'] = items['product_name']
                product['product_description'] = items['product_description']
                product['product_category_id'] = items['product_category_id__category_id']
                product['product_category_name'] = items['product_category_id__category_name']
                product['product_sku'] = items['product_sku']
                product['product_price'] = items['product_discount_price']
                product['product_quantity'] = items['product_stock']
                product['product_status'] = 'Active' if items['product_status'] == 'Y' else 'Inactive'

                res_products.append(product)

            paginator = Paginator(range(product_list['data_count']), per_page)
            try:
                page_obj = paginator.page(page_number)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

            result['product_list'] = res_products
            result['product_count'] = product_list['data_count']

            result['product_obj'] = {}
            result['product_obj']['pagination_count'] = math.ceil(product_list['data_count'] / per_page)
            result['product_obj']['current_page'] = page_obj.number
            result['product_obj']['has_previous'] = page_obj.has_previous()
            result['product_obj']['has_next'] = page_obj.has_next()
            result['product_obj']['previous_page_number'] = page_obj.previous_page_number() if page_obj.has_previous() else None
            result['product_obj']['next_page_number'] = page_obj.next_page_number() if page_obj.has_next() else None
            result['product_obj']['start_index'] = page_obj.start_index()
            result['product_obj']['end_index'] = page_obj.end_index()

            return JsonResponse(result, status=200)
        
        res_error = {}
        res_error['message'] = 'Wrong method has been envoked'
        
        return JsonResponse(res_error, status=400)

    except Exception as ex:
        logger.error(ex)


@Authentication.inventory_login_decorator
def inventory_add_products(request):
    try:
        context = {}
        context['active_menu_item'] = 'Add Products'
        
        return render(request, 'inventory/view_inventory_add_products.html', context)

    except Exception as ex:
        logger.error(ex)
