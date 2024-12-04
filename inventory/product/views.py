import logging
from .forms import *
from .models import *
from django.conf import settings
from django.shortcuts import render
from common.utils import Authentication
from shopease.settings import get_logging_config

# Logger details
settings.LOGGING = get_logging_config(__name__)
logger = logging.getLogger(__name__)


@Authentication.inventory_login_decorator
def inventory_view_products(request):
    try:
        context = {}
        context['active_menu_item'] = 'Product Listing'

        return render(request, '', context)

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
