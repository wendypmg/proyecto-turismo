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
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

def index(request):
    return render(request, "blog/index.html")

def restaurantes(request):
    restaurantes = Restaurante.objects.all()

    context_dict = {
        'restaurantes': restaurantes
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog/restaurante.html"
    )

def sitios(request):
    sitios = Sitio.objects.all()

    context_dict = {
        'sitios': sitios
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog/sitio.html"
    )

def monumentos(request):
    monumentos = Monumento.objects.all()

    context_dict = {
        'monumentos': monumentos
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog/monumento.html"
    )

def form_html(request):

    if request.method == 'POST':
        restaurante = Restaurante(nombre=request.POST['nombre'], ciudad=request.POST['ciudad'])
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

    return render(
        request=request,
        template_name='blog/formHTML.html'
    )

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

# -------CRUD RESTAURANTE
def update_restaurante(request, pk: int):
    restaurante = Restaurante.objects.get(pk=pk)

    if request.method == 'POST':
        restaurante_form = RestauranteForm(request.POST)
        if restaurante_form.is_valid():
            data = restaurante_form.cleaned_data
            restaurante.nombre = data['nombre']
            restaurante.ciudad = data['ciudad']
            restaurante.tipo_de_comida = data['tipo_de_comida']
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

    restaurante_form = RestauranteForm(model_to_dict(restaurante))
    context_dict = {
        'restaurante': restaurante,
        'restaurante_form': restaurante_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/restaurante_form.html'
    )

def delete_restaurante(request, pk: int):
    restaurante = Restaurante.objects.get(pk=pk)
    if request.method == 'POST':
        restaurante.delete()

        restaurantes = Restaurante.objects.all()
        context_dict = {
            'restaurantes': restaurantes
        }
        return render(
            request=request,
            context=context_dict,
            template_name="blog/restaurante.html"
        )

    context_dict = {
        'restaurante': restaurante,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/restaurante_confirm_delete.html'
    )

#CRUD MONUMENTO
def update_monumento(request, pk: int):
    monumento = Monumento.objects.get(pk=pk)

    if request.method == 'POST':
        monumento_form = MonumentoForm(request.POST)
        if monumento_form.is_valid():
            data = monumento_form.cleaned_data
            monumento.nombre = data['nombre']
            monumento.ciudad = data['ciudad']
            monumento.fecha = data['fecha']
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

    monumento_form = MonumentoForm(model_to_dict(monumento))
    context_dict = {
        'monumento': monumento,
        'monumento_form': monumento_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/monumento_form.html'
    )

def delete_monumento(request, pk: int):
    monumento = Monumento.objects.get(pk=pk)
    if request.method == 'POST':
        monumento.delete()

        monumentos = Monumento.objects.all()
        context_dict = {
            'monumentos': monumentos
        }
        return render(
            request=request,
            context=context_dict,
            template_name="blog/monumento.html"
        )

    context_dict = {
        'monumento': monumento,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/monumento_confirm_delete.html'
    )

#-------CRUD SITIOS
def update_sitio(request, pk: int):
    sitio = Sitio.objects.get(pk=pk)

    if request.method == 'POST':
        sitio_form = SitioForm(request.POST)
        if sitio_form.is_valid():
            data = sitio_form.cleaned_data
            sitio.nombre = data['nombre']
            sitio.ciudad = data['ciudad']
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

    sitio_form = SitioForm(model_to_dict(sitio))
    context_dict = {
        'sitio': sitio,
        'sitio_form': sitio_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/sitio_form.html'
    )

#ELIMINAR
def delete_sitio(request, pk: int):
    sitio = Sitio.objects.get(pk=pk)
    if request.method == 'POST':
        sitio.delete()

        sitios = Sitio.objects.all()
        context_dict = {
            'sitios': sitios
        }
        return render(
            request=request,
            context=context_dict,
            template_name="blog/sitio.html"
        )

    context_dict = {
        'sitio': sitio,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/sitio_confirm_delete.html'
    )

#RESTAURANTE

class RestauranteListView(ListView):
    model = Restaurante
    template_name = "blog/restaurante_list.html"

class RestauranteDetailView(DetailView):
    model = Restaurante
    template_name = "blog/restaurante_detail.html"

class RestauranteCreateView(CreateView):
    model = Restaurante
    success_url = reverse_lazy('blog:restaurante-list')
    fields = ['nombre', 'ciudad', 'tipo_de_comida']

class RestauranteUpdateView(UpdateView):
    model = Restaurante
    success_url = reverse_lazy('blog:restaurante-list')
    fields = ['nombre', 'ciudad', 'tipo_de_comida']

class RestauranteDeleteView(DeleteView):
    model = Restaurante
    success_url = reverse_lazy('blog:restaurante-list')

#MONUMENTO

class MonumentoListView(ListView):
    model = Monumento
    template_name = "blog/monumento_list.html"

class MonumentoDetailView(DetailView):
    model = Monumento
    template_name = "blog/monumento_detail.html"

class MonumentoCreateView(CreateView):
    model = Monumento
    success_url = reverse_lazy('blog:monumento-list')
    fields = ['nombre', 'ciudad', 'fecha']

class MonumentoUpdateView(UpdateView):
    model = Monumento
    success_url = reverse_lazy('blog:monumento-list')
    fields = ['nombre', 'ciudad', 'fecha']

class MonumentoDeleteView(DeleteView):
    model = Monumento
    success_url = reverse_lazy('blog:monumento-list')

#SITIO

class SitioListView(ListView):
    model = Sitio
    template_name = "blog/sitio_list.html"

class SitioDetailView(DetailView):
    model = Sitio
    template_name = "blog/sitio_detail.html"

class SitioCreateView(CreateView):
    model = Sitio
    success_url = reverse_lazy('blog:sitio-list')
    fields = ['nombre', 'ciudad']

class SitioUpdateView(UpdateView):
    model = Sitio
    success_url = reverse_lazy('blog:sitio-list')
    fields = ['nombre', 'ciudad']

class SitioDeleteView(DeleteView):
    model = Sitio
    success_url = reverse_lazy('blog:sitio-list')

#LOGIN - PRUEBA
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("blog:user-login")
    form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="blog/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home:main")

        return render(
            request=request,
            context={'form': form},
            template_name="blog/login.html",
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="blog/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("blog:user-login")


@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            return redirect('blog:main')

    form= UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="blog/user_form.html",
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
            return redirect('blog:main')

    form= AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="blog/avatar_form.html",
    )


#DECORADOR

@login_required
def inicio(request):
    return render(request, "blog/home.html")




