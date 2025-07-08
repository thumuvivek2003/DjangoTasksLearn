from django.http import HttpResponse

def hello_view(request):
    return HttpResponse('Hello World!!')

def hello_vivek(request):
    return HttpResponse('Hello Vivek!!')