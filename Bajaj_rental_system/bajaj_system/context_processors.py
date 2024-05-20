
from .models import *
from django.shortcuts import redirect

def user_profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = Customer.objects.get(id=user_id)
        return {'user': user}
    return {}
