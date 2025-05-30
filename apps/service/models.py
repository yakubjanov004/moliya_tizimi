from django.db import models
from apps.core.models import BaseModel

class Ombor(BaseModel):
    sotilganlik_sanasi = models.DateField()
    olinganlik_sanasi = models.DateField()
    nomi = models.CharField(max_length=100)
    miqdori = models.IntegerField()
    narx = models.IntegerField()
    ustama = models.IntegerField()
    sotilganlar_miqdori = models.IntegerField()
    jami_tovar = models.IntegerField()
    sotilgan_tovar_summasi = models.IntegerField()
    qoldiq_tovar_soni = models.IntegerField()
    qoldiq_tovar_summasi = models.IntegerField()
    tovar_uchun_foyda = models.IntegerField()

class EskirishShablon(BaseModel):
    sana = models.DateField()
    nomi = models.CharField(max_length=100)
    summa = models.IntegerField()
    yillik_summa = models.IntegerField()
    oylik_summa = models.IntegerField()
    eskirish_foiz = models.IntegerField()
    eskirgan_oylar_soni = models.IntegerField()
    joriy_eskirgan_summa = models.IntegerField()
    qoldiq_qiymat = models.IntegerField()

class OylikHisobot(BaseModel):
    sana = models.DateField()
    fio = models.CharField(max_length=100)
    ish_haqi = models.IntegerField()
    JSHSHIR_foiz = models.IntegerField()
    JSHSHIR_summa = models.IntegerField()
    soliq_foiz = models.IntegerField()
    soliq_summa = models.IntegerField()
    inps_foiz = models.IntegerField()
    inps_summa = models.IntegerField()
    tolanadigan_summa = models.IntegerField()
    avans = models.IntegerField()
    hodim_qarzi = models.IntegerField()

class Work(BaseModel):
    nomi = models.CharField(max_length=100)
    narxi = models.IntegerField()
    iconncha = models.CharField(max_length=100, null=True, blank=True)
    descr = models.TextField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nomi