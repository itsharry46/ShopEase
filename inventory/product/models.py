from django.db.models import Count
from common.models import Category


def model_get_category_list():
    try:
        queryset = Category.objects.filter(category_status = 'Y', product__product_status = 'Y'). \
            annotate(product_count=Count('product__product_id')). \
            select_related('product_category_id'). \
            values('category_id', 'category_name', 'category_description', 'product_count')
        
        queryset = queryset.all()

        return queryset

    except Exception as ex:
        print('model_get_category_list exception => ', ex)
