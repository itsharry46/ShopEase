from django.db import transaction
from common.models import Category
from django.db.models import Count, Q


def model_get_category_list():
    try:
        queryset = Category.objects.filter(category_status = 'Y'). \
            annotate(product_count=Count('product__product_id')). \
            select_related('product_category_id'). \
            values('category_id', 'category_name', 'category_description', 'product_count')
        
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

