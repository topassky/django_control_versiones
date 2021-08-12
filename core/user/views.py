from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from core.user.models import User


class UserView(TemplateView):
    template_name = 'user.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Página principal'
        context['dashboard_url'] = reverse_lazy('index')
        return context



