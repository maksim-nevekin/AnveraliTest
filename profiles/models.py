from datetime import timezone
from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)    
    experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().delete(*args, **kwargs)    


class Сustomer(BaseModel):
    abstract = False


class Executor(BaseModel):
    abstract = False
