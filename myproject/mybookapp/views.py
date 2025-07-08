from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello, this is the home page!")

def about_view(request):
    return HttpResponse("About us page")

def contact_view(request):
    return HttpResponse("Contact us page")
