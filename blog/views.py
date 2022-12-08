from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.db.models import Q
from django.forms.models import model_to_dict

from blog.models import *
from blog.forms import *

from django.urls import reverse_lazy
#VIEWS ESPCIALES
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#AUTENTICACION
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

def index(request):
    return render(request, "blog/index.html")

@login_required
def restaurante_forms_django(request):
    if request.method == 'POST':
        restaurante_form = RestauranteForm(request.POST)
        if restaurante_form.is_valid():
            data = restaurante_form.cleaned_data
            restaurante = Restaurante(nombre=data['nombre'], ciudad=data['ciudad'], tipo_de_comida=data['tipo_de_comida'])
            restaurante.save()

            restaurantes = Restaurante.objects.all()
            context_dict = {
                'restaurantes': restaurantes
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog/restaurante.html"
            )

    restaurante_form = RestauranteForm(request.POST)
    context_dict = {
        'restaurante_form': restaurante_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/restaurante_django_forms.html'
    )

@login_required
def monumento_forms_django(request):
    if request.method == 'POST':
        monumento_form = MonumentoForm(request.POST)
        if monumento_form.is_valid():
            data = monumento_form.cleaned_data
            monumento = Monumento(nombre=data['nombre'], ciudad=data['ciudad'], fecha=data['fecha'])
            monumento.save()

            monumentos = Monumento.objects.all()
            context_dict = {
                'monumentos': monumentos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog/monumento.html"
            )

    monumento_form = MonumentoForm(request.POST)
    context_dict = {
        'monumento_form': monumento_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/monumento_django_forms.html'
    )

@login_required
def sitio_forms_django(request):
    if request.method == 'POST':
        sitio_form = SitioForm(request.POST)
        if sitio_form.is_valid():
            data = sitio_form.cleaned_data
            sitio = Sitio(nombre=data['nombre'], ciudad=data['ciudad'])
            sitio.save()

            sitios = Sitio.objects.all()
            context_dict = {
                'sitios': sitios
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog/sitio.html"
            )

    sitio_form = SitioForm(request.POST)
    context_dict = {
        'sitio_form': sitio_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/sitio_django_forms.html'
    )

#RESTAURANTE

class RestauranteListView(ListView):
    model = Restaurante
    template_name = "blog/restaurante_list.html"

class RestauranteDetailView(DetailView):
    model = Restaurante
    template_name = "blog/restaurante_detail.html"

class RestauranteCreateView(LoginRequiredMixin, CreateView):
    model = Restaurante
    success_url = reverse_lazy('blog:restaurante-list')
    fields = ['nombre', 'ciudad', 'tipo_de_comida', 'experiencia', 'image']

    def form_valid(self, form):
        """Add owner to the new restaurante object"""
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RestauranteUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurante
    success_url = reverse_lazy('blog:restaurante-list')
    fields = ['nombre', 'ciudad', 'tipo_de_comida', 'experiencia', 'image']

class RestauranteDeleteView(LoginRequiredMixin, DeleteView):
    model = Restaurante
    success_url = reverse_lazy('blog:restaurante-list')

#MONUMENTO

class MonumentoListView(ListView):
    model = Monumento
    template_name = "blog/monumento_list.html"

class MonumentoDetailView(DetailView):
    model = Monumento
    template_name = "blog/monumento_detail.html"

class MonumentoCreateView(LoginRequiredMixin, CreateView):
    model = Monumento
    success_url = reverse_lazy('blog:monumento-list')
    fields = ['nombre', 'ciudad', 'descripcion', 'historia', 'image']

    def form_valid(self, form):
        """Add owner to the new restaurante object"""
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MonumentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Monumento
    success_url = reverse_lazy('blog:monumento-list')
    fields = ['nombre', 'ciudad', 'descripcion', 'historia', 'image']

class MonumentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Monumento
    success_url = reverse_lazy('blog:monumento-list')

#SITIO

class SitioListView(ListView):
    model = Sitio
    template_name = "blog/sitio_list.html"

class SitioDetailView(DetailView):
    model = Sitio
    template_name = "blog/sitio_detail.html"

class SitioCreateView(LoginRequiredMixin, CreateView):
    model = Sitio
    success_url = reverse_lazy('blog:sitio-list')
    fields = ['nombre', 'ciudad', 'descripcion', 'historia', 'image']
       
    def form_valid(self, form):
        """Add owner to the new restaurante object"""
        form.instance.owner = self.request.user
        return super().form_valid(form)

class SitioUpdateView(LoginRequiredMixin, UpdateView):
    model = Sitio
    success_url = reverse_lazy('blog:sitio-list')
    fields = ['nombre', 'ciudad', 'descripcion', 'historia', 'image']

class SitioDeleteView(LoginRequiredMixin, DeleteView):
    model = Sitio
    success_url = reverse_lazy('blog:sitio-list')

#LOGIN - PRUEBA
def register(request):
    form = UserRegisterForm(request.POST) if request.POST else UserRegisterForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("blog:login")

    return render(
        request=request,
        context={"form": form},
        template_name="registration/register.html",
    )


@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:Home')

    form= UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="registration/user_form.html",
    )

#AVATAR
def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"avatar_url": avatars[0].image.url}
    return {}


def index(request):
    return render(
        request=request,
        context=get_avatar_url_ctx(request),
        template_name="blog/index.html",
    ) 


@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('blog:Home')

    form= AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="registration/avatar_form.html",
    )


#DECORADOR

@login_required
def inicio(request):
    return render(request, "blog/home.html")






