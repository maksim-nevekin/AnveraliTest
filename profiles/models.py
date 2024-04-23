from datetime import timezone
from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    second_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.IntegerField(verbose_name="Номер телефона")
    email = models.EmailField(max_length=254, verbose_name="Адрес электронной почты")
    experience = models.IntegerField(verbose_name="Опыт работы")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name[0]}.{self.second_name}"

    class Meta:
        abstract = True


class Customer(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        abstract = False
        verbose_name ='заказчика'
        verbose_name_plural ='Заказчики'


class Executor(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        abstract = False
        verbose_name ='исполнителя'
        verbose_name_plural ='Исполнители'
