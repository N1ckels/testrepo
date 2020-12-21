from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us!",
        "my_number": "1234",
        "my_list": [123, 4242, 123123, 65555]
    }
    return render(request, "about.html", my_context)
