from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from apps.post.models import Post


def blogPost(request, post_id):
	context = {'post': Post.objects.get(id=post_id)}
	return TemplateResponse(request, 'post/blog-post.html', context)