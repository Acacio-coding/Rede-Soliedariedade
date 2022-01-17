from django.http import HttpResponse
from django.shortcuts import redirect

def not_auth(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function

def is_auth(view_function):
    def wrapper_function(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function

def allowed(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            if  request.user.is_superuser:
                return view_function(request, *args, **kwargs)
            else:
                groups = None
                if request.user.groups.exists():
                    groups = request.user.groups.all().name

                    can = False
                    for group in groups:
                        if group in allowed_roles:
                            can = True

                    if can:
                        return view_function(request, *args, **kwargs)
                    else:
                        return redirect('/')
                else:
                    return redirect('/')
                     
        return wrapper_function 

    return decorator