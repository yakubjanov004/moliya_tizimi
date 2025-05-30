from django.db import models
from apps.core.models import BaseModel
from apps.users.models import UserModel

class Korxona(BaseModel):
    nomi = models.CharField(max_length=100)
    inn = models.BigIntegerField(unique=True)
    location = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    ish_faoliyati = models.CharField(max_length=255)
    email = models.EmailField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi