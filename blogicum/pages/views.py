from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CreationForm
from django.shortcuts import render

class RegistrationView(CreateView):
    form_class = CreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('blog:index')


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    return render(request, 'pages/500.html', status=500)
