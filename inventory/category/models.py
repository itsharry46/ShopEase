from django.db import transaction
from django.db.models import Count
from common.utils import CustomLogging

from common.models import Category

# Logger details
logger = CustomLogging.setup_logger(__name__)


def model_get_category_list(filters):
    try:
        queryset = Category.objects. \
            annotate(product_count=Count('product__product_id')). \
            select_related('product_category_id'). \
            values('category_id', 'category_name', 'category_description', 'product_count', 'category_status'). \
            order_by('category_status')
        
        if filters['search_category']:
            queryset = queryset.filter(category_name__icontains = filters['search_category'])
        
        queryset = queryset.all()

        return queryset

    except Exception as ex:
        err_message = 'model_get_category_list exception => ' + ex
        logger.error(err_message)


def model_add_category(add_category):
    try:
        with transaction.atomic():
            new_category = Category(**add_category)
            new_category.save()

        return True

    except Exception as ex:
        err_message = 'model_add_category exception => ' + ex
        logger.error(err_message)
        return False


def model_update_category_information(category_id):
    try:
        queryset = Category.objects.filter(category_id = category_id). \
            values('category_name', 'category_description', 'category_status')

        queryset.first()

        return queryset

    except Exception as ex:
        err_message = 'model_update_category_information' + ex
        logger.error(err_message)


def model_update_category(category_id, category_data):
    try:
        with transaction.atomic():
            updated_count = Category.objects.filter(category_id = category_id). \
                update(**category_data)
            
            if updated_count > 0:
                return True
            else:
                raise Exception(f"Failed to update category id {category_id}")

    except Exception as ex:
        err_message = 'model_update_category exception => ' + ex
        logger.error(err_message)
        return False
    

def model_delete_category(category_id):
    try:
        with transaction.atomic():
            updated_count = Category.objects.filter(category_id = category_id). \
                update(category_status = 'N')
            
            if updated_count > 0:
                return True
            else:
                raise Exception(f"Failed to delete category id {category_id}")

    except Exception as ex:
        err_message = 'model_delete_category' + ex
        logger.error(err_message)
