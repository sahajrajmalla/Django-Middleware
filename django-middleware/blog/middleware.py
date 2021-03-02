from django.shortcuts import HttpResponse

class MyProcessMiddleware:
    def __init__(self, get_response):
        print('This is process middleware')
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        print('This is process view just before view')

        # We we return HttpResponse, the view will not be executed
        # We we return None, the view will be executed

    def process_exception(self, request, exception):
        print('Exception Occured')
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)

        return HttpResponse(msg)

    def process_template_response(self, request, response):
        print('This is process template response')
        response.context_data['name'] = 'Sonam'
        return response



def my_middleware(get_response):
    print('One Time function-based Initiailzation ')

    def my_function(request):
        print('This is before view by function-based')
        # If i put the HttpResponse here, the view.py will not be
        # responded neither will below middleware according to the order in settings.py
        response = get_response(request)
        print("This is after view by function-based")
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


