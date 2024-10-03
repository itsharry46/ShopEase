import logging
from django.conf import settings
from django.shortcuts import render
from shopease.settings import get_logging_config

# Logger details
settings.LOGGING = get_logging_config(__name__)
logger = logging.getLogger(__name__)


def inventory_login(request):
    try:
        return render(request, 'inventory/view_inventory_login.tml')

    except Exception as ex:
        logger.error(f'=> Error Log Raised => {ex}')
        print(ex)