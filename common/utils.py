from django.shortcuts import redirect

class Authentication:

    @staticmethod
    def inventory_login_decorator(func):
        def _wrapper_view(request):
            
            if 'user_logged_in' in request.session and 'role_id' in request.session:
                if request.session['role_id'] in [1, 2] and request.session['user_logged_in'] == True:
                    result = func(request)
                    return result
                
                # Comment Redirect to wrong access page

            return redirect('inventory_logout')
        
        return _wrapper_view