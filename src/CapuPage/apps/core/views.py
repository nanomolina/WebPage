 # -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from django.template import RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from apps.core.models import *
from apps.core.functions import loginFormToContext
from apps.post.models import Post


def home(request):
    slide = Slide.objects.get(active=True)
    main_content = MainContent.objects.get(active=True)
    context = {'images': slide.getVisibleImages,
               'main_content': main_content,
               'posts': Post.objects.order_by('created')}
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
    print request
    auth_logout(request)
    response = redirect('core:home')
    return response
