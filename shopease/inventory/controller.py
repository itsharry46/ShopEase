import hashlib
from .models import *


def controller_validate_user_login(username, password):
    try:
        password = hashlib.md5(password.encode()).hexdigest()
        res_user_details = model_get_user_details(username, password)
        if not res_user_details:
            return 400, "Invalid login credentials"
        
        return 200, res_user_details
    
    except Exception as ex:
        print(ex)
