from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('user_id') and request.path not in ['/login/', '/logout/']:
            return redirect('login_page')
        return self.get_response(request)



class AdminRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin_dashboard/') and not request.session.get('is_admin'):
            return redirect('login')
        response = self.get_response(request)
        return response
