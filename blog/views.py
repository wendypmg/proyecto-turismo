from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.db.models import Q
from django.forms.models import model_to_dict

from blog.models import Restaurante, Sitio, Monumento
from blog.forms import RestauranteForm, SitioForm, MonumentoForm

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "blog/home.html")

def restaurantes(request):
    restaurantes = Restaurante.objects.all()

    context_dict = {
        'restaurantes': restaurantes
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog/restaurantes.html"
    )

def sitios(request):
    sitios = Sitio.objects.all()

    context_dict = {
        'sitios': sitios
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog/sitios.html"
    )

def monumentos(request):
    monumentos = Monumento.objects.all()

    context_dict = {
        'monumentos': monumentos
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog/monumentos.html"
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
            template_name="blog/restaurantes.html"
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
                template_name="blog/restaurantes.html"
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
                template_name="blog/monumentos.html"
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
                template_name="blog/sitios.html"
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
                template_name="blog/restaurantes.html"
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
            template_name="blog/restaurantes.html"
        )

    context_dict = {
        'restaurante': restaurante,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/restaurante_confirm_delete.html'
    )

#-------CRUD MONUMENTO
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
                template_name="blog/monumentos.html"
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
            template_name="blog/monumentos.html"
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
                template_name="blog/sitios.html"
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
            template_name="blog/sitios.html"
        )

    context_dict = {
        'sitio': sitio,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/sitio_confirm_delete.html'
    )

def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        restaurantes = Restaurante.objects.filter(universidad__contains=search_param)
        context_dict = {
            'restaurantes': restaurantes
        }

    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(universidad__contains=search_param)
        restaurantes = Restaurante.objects.filter(query)
        context_dict = {
            'restaurante': restaurantes
        }

    return render(
        request=request,
        context=context_dict,
        template_name="blog/home.html",
    )

#----------RESTAURANTE

class RestauranteListView(ListView):
    model = Restaurante
    template_name = "blog/restaurante_list.html"

class RestauranteDetailView(DetailView):
    model = Restaurante
    template_name = "blog/restaurante_detail.html"

class RestauranteCreateView(CreateView):
    model = Restaurante
    success_url = reverse_lazy('blog:restaurante-list')
    fields = ['universidad', 'anio_inicio', 'titulo', 'finalizado']

class RestauranteUpdateView(UpdateView):
    model = Restaurante
    success_url = reverse_lazy('blog:restaurante-list')
    fields = ['universidad', 'anio_inicio', 'titulo', 'finalizado']

class RestauranteDeleteView(DeleteView):
    model = Restaurante
    success_url = reverse_lazy('blog:restaurante-list')

#-----------MONUMENTO

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

#----------SITIOS

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
