from django.db.models.signals import pre_save, pre_delete, post_delete, post_save
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio


def car_inventory_update():
    total_cars_count = Car.objects.all().count()
    sum_cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']
    CarInventory.objects.create(cars_count=total_cars_count, cars_value= sum_cars_value)


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delte(sender, instance, **kwargs):   
    car_inventory_update()


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    '''
    Função para gerar descrição com a api do oOpenIA (desativada pois a API é paga):
    if not instance.description:
        ai_description = get_car_ai_bio(
            instance.model, instance.brand, instance.model_year
        )
        instance.description = ai_description
    '''
    pass


#@receiver(pre_delete, sender=Car)
#def car_post_delete(sender, instance, **kwargs):   
#    print(instance.model, instance.brand)
#    pass