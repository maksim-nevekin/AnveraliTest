from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    # name = models.CharField(max_length=50, blank=False, verbose_name="Имя")
    # second_name = models.CharField(max_length=50, verbose_name="Фамилия")
    # username = models.CharField(max_length=50, verbose_name="Пс")
    phone_number = models.IntegerField(blank=True, null=True, verbose_name="Номер телефона")
    # email = models.EmailField(max_length=254, blank=False, verbose_name="Адрес электронной почты")
    # experience = models.IntegerField(verbose_name="Опыт работы")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username
    


# class Customer(BaseModel):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     class Meta:
#         abstract = False
#         verbose_name ='заказчика'
#         verbose_name_plural ='Заказчики'


# class Executor(BaseModel):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     class Meta:
#         abstract = False
#         verbose_name ='исполнителя'
#         verbose_name_plural ='Исполнители'
