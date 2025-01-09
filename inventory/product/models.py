from django.db.models import Count
from common.utils import CustomLogging

from common.models import Category, Product

# Logger details
logger = CustomLogging.setup_logger(__name__)


def model_get_category_list():
    try:
        queryset = Category.objects. \
            annotate(product_count=Count('product__product_id')). \
            select_related('product_category_id'). \
            values('category_id', 'category_name', 'category_description', 'product_count', 'category_status'). \
            order_by('category_status')
        
        queryset = queryset.all()

        return queryset

    except Exception as ex:
        err_message = 'model_get_category_list exception => ' + ex
        logger.error(err_message)


def model_get_product_list(offset, limit, filters):
    try:
        base_queryset = Product.objects.select_related('product_category_id')

        # Filters
        if filters['category_status'] != 'None':
            base_queryset = base_queryset.filter(product_category_id__category_status = filters['category_status'])

        if filters['product_category'] != 'None':
            base_queryset = base_queryset.filter(product_category_id = filters['product_category'])

        if filters['product_stock_status'] != 'None':
            base_queryset = base_queryset.filter(product_status = filters['product_stock_status'])
        
        if filters['search_product']:
            base_queryset = base_queryset.filter(product_name__icontains = filters['search_product'])

        # Getting total records
        queryset_count = base_queryset.count()

        # Get paginated results
        queryset = (base_queryset.values('product_id', 'product_name', 'product_description', 'product_category_id__category_id', 'product_category_id__category_name', 'product_sku', 'product_discount_price', 'product_stock', 'product_status'). \
            order_by('-product_id')[offset:limit])
        
        queryset = queryset.all()

        result = {}
        result['data_count'] = queryset_count
        result['data_item'] = queryset

        return result

    except Exception as ex:
        err_message = 'model_get_product_list exception => ' + ex
        logger.error(err_message)