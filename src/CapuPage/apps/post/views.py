from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from apps.post.models import Post, Category
from apps.post.functions import get_categories


def blogPost(request, post_id):
    categories_1, categories_2 = get_categories()
    context = {'post': Post.objects.get(id=post_id),
               'categories_1': categories_1,
               'categories_2': categories_2}
    return TemplateResponse(request, 'post/blog-post.html', context)


def blogCategory(request, category_num):
    categories_1, categories_2 = get_categories()
    category = Category.objects.get(number=category_num)
    context = {'posts': Post.objects.filter(category=category),
               'categories_1': categories_1,
               'categories_2': categories_2,
               'category': category}
    return TemplateResponse(request, 'post/blog-category.html', context)
