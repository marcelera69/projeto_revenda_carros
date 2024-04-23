from django.db.models.query import QuerySet
from cars.models import Car, CarWish
from cars.forms import CarForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


def is_superuser(user):
    return user.is_superuser


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



class CarWishListView(LoginRequiredMixin, ListView):
    model = CarWish
    template_name = 'cars_wish.html'
    context_object_name = 'wish_list'


@login_required(login_url='login')
def add_car_to_wishlist(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car_wish, created = CarWish.objects.get_or_create(user=request.user)
    car_wish.cars.add(car)
    return redirect('cars_wish')  


class NewCarView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'

    def test_func(self):
        return is_superuser(self.request.user)



class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        return is_superuser(self.request.user)
    


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

    def test_func(self):
        return is_superuser(self.request.user)

