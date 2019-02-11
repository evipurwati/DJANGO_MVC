from django.db.models import CharField
from django.db.models import TextField

from django.db import models as models

class Hewan(models.Model) :
    nama = models.CharField(max_length = 255)
    species = models.TextField(max_length = 255)
    berat = models.CharField(max_length = 55)
    umur = models.CharField(max_length = 55)

class Kandang(models.Model) :
    nama = models.CharField(max_length = 255)
    isi_kandang = models.CharField(max_length = 255)
    luas_kandang = models.CharField(max_length = 55)

class Penjaga(models.Model) :
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 25)
    jadwal_jaga = models.CharField(max_length = 55)

class Pengunjung(models.Model) :
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 25)
    hari_berkunjung = models.TextField(max_length = 55)