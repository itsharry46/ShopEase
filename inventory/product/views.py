from .forms import *
from .models import *
from django.shortcuts import render
from common.utils import Authentication, CustomLogging

# Logger details
logger = CustomLogging.setup_logger(__name__)


@Authentication.inventory_login_decorator
def inventory_view_products(request):
    try:
        context = {}
        context['active_menu_item'] = 'Product Listing'

        category_list = model_get_category_list()
        res_category = []
        res_category.append({'category_id': 0, 'category_name': 'Select Product Category'})
        for category_item in category_list:
            category = {}
            category['category_id'] = category_item['category_id']
            category['category_name'] = category_item['category_name']

            res_category.append(category)

        
        context['category_list'] = res_category

        category_status = []
        category_status.append({'category_status_id': 0, 'category_status': 'Select Category Status'})
        category_status.append({'category_status_id': 'Y', 'category_status': 'Active'})
        category_status.append({'category_status_id': 'N', 'category_status': 'Inactive'})
        context['category_status'] = category_status

        category_stock = []
        category_stock.append({'stock_id': 0, 'stock_status': 'Select Product Stock Status'})
        category_stock.append({'stock_id': 'Y', 'stock_status': 'In Stock'})
        category_stock.append({'stock_id': 'N', 'stock_status': 'Out Of Stock'})
        context['category_stock_status'] = category_stock

        product_list = model_get_product_list(10, 30)
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

        context['product_list'] = res_products

        return render(request, 'inventory/view_inventory_view_products.html', context)

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
