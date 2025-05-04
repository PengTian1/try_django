from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, world! This is the homepage.")


# This is a simple Django view that returns a plain text response.
# It can be used to test the URL routing in the Django application.
# The view function takes an HTTP request as an argument and returns an HTTP response.
# The response contains a simple message indicating that this is the about page.
# The view function can be used in the URL configuration to map a specific URL pattern to this view.
def about(request):
    return HttpResponse("This is the about page.")
