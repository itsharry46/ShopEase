from django.shortcuts import redirect

class InventorySessionRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define which paths should be protected
        protected_paths = ['/inventory/dashboard/']

        if request.path in protected_paths and 'user_logged_in' not in request.session:
            return redirect('inventory_login')
        
        if request.path == '/inventory/' and 'user_logged_in' in request.session:
            return redirect('/inventory/dashboard')
        
        response = self.get_response(request)
        return response
