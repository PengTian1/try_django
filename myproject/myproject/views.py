#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    context = {
        'title': 'Welcome to My Django App',
        'message': 'This is the homepage of my Django application.',
    }
    return render(request, 'home.html', context)
    #return HttpResponse("Hello, world! This is the homepage.")


# This is a simple Django view that returns a plain text response.
# It can be used to test the URL routing in the Django application.
# The view function takes an HTTP request as an argument and returns an HTTP response.
# The response contains a simple message indicating that this is the about page.
# The view function can be used in the URL configuration to map a specific URL pattern to this view.
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is the about page.")
