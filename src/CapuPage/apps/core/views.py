from django.template.response import TemplateResponse
from apps.core.models import Slide, SlideImage

def home(request):
    slide = Slide.objects.get(active=True)
    images = SlideImage.objects.filter(slide__name=slide)
    slide_images = []
    for image in images:
        if image.show_image is True:
            slide_images.append(image)
    context = {'images': slide_images}
    return TemplateResponse(request, 'core/home.html', context)
