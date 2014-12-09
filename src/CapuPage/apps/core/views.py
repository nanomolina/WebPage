 # -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from django.template import RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from apps.core.models import Slide, SlideImage
from apps.core.functions import loginFormToContext


def home(request):
    slide = Slide.objects.get(active=True)
    images = SlideImage.objects.filter(slide__name=slide)
    slide_images = []
    for image in images:
        if image.show_image is True:
            slide_images.append(image)
    context = {'images': slide_images}
    context = loginFormToContext(request, context)
    return TemplateResponse(request, 'core/home.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('core:home')
        else:
          return HttpResponse("")


def logout(request):
    auth_logout(request)
    response = redirect('core:home')
    return response
