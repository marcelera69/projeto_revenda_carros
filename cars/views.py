from django.db.models.query import QuerySet
from cars.models import Car
from cars.forms import CarForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search).order_by('model')

        return cars

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quantidade_carros'] = self.get_queryset().count()
        return context


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class NewCarView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'



class CarUpdateView(LoginRequiredMixin,  UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

    

