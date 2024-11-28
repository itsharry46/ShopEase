from django.db import transaction
from common.models import Category
from django.db.models import Count, Q


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
        print('model_get_category_list exception => ', ex)


def model_add_category(add_category):
    try:
        with transaction.atomic():
            new_category = Category(**add_category)
            new_category.save()

        return True

    except Exception as ex:
        print('model_add_category exception => ', ex)
        return False


def model_update_category_information(category_id):
    try:
        queryset = Category.objects.filter(category_id = category_id). \
            values('category_name', 'category_description', 'category_status')

        queryset.first()

        return queryset

    except Exception as ex:
        print('model_update_category_information', ex)

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
        print('model_update_category exception => ', ex)
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
        print('model_delete_category', ex)
