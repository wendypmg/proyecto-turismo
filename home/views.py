from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User


from blog.models import Avatar

def home(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html"
    )

def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}

def AboutWendyView(request):
    return render(
        request=request,
        template_name="home/wendy.html",
    )

def AboutAngelicaView(request):
    return render(
        request=request,
        template_name="home/angelica.html",
    )

def AboutSofiaView(request):
    return render(
        request=request,
        template_name="home/sofia.html",
    )
