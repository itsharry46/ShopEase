import logging
from django.conf import settings
from django.shortcuts import render
from common.utils import Authentication
from shopease.settings import get_logging_config

# Logger details
settings.LOGGING = get_logging_config(__name__)
logger = logging.getLogger(__name__)


@Authentication.inventory_login_decorator
def inventory_dashboard(request):
    try:

        context = {}
        context['active_menu_item'] = 'Dashboard'
        
        return render(request, 'inventory/view_inventory_dashboard.html', context)

    except Exception as ex:
        logger.error(ex)
