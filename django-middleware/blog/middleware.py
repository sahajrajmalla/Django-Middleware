from django.shortcuts import HttpResponse

def my_middleware(get_response):
    print('One Time function-based Initiailzation ')
    def my_function(request):
        print('This is before view by function-based')
        #If i put the HttpResponse here, the view.py will not be responded neither will below middleware according to the order in settings.py
        response = get_response(request)
        print('This is after view by function-based')
        return response
    return my_function

class MeroMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('One Time Class-based Initialization')

    def __call__(self, request):
        print('This is before view by Class-based')
        response = self.get_response(request)
        print('This is after view by Class-based')
        return response
