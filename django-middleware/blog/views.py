from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print('I am view')
    return HttpResponse('I am view')

# def excep(request):
#     print('I am excep view')
#     a = 10/0
#     return HttpResponse('This is excep page {}'.format(a))


def user_info(request):
    print('I am user info view')
    context = {
        'name': 'Rahul'
    }
    return TemplateResponse(request, 'blog/user.html', context)