from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hello, world! This is the hello page of myapp.')
#
# This is a simple Django view that returns a plain text response.
# It can be used to test the URL routing in the Django application.

from django.views.generic import TemplateView
class MyView(TemplateView):
    template_name = 'hello.html'

from django.shortcuts import render
def posts_list(request):
    return render(request, 'myapp/posts_list.html')