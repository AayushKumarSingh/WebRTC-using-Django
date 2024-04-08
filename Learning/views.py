from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.


def homepage_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def social_view(request, *args, **kwargs):
    content = loader.render_to_string("socials.html", context=None, request=request, using=None)
    return HttpResponse(content, content_type=None, status=None)
