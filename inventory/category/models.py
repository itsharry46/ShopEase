import logging
from django.conf import settings
from django.db import transaction
from django.db.models import Count
from shopease.settings import get_logging_config

from common.models import Category

# Logger details
settings.LOGGING = get_logging_config(__name__)
logger = logging.getLogger(__name__)


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
        print(err_message)
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
        print(err_message)
