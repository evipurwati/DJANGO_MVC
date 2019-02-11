# from django.db import models

from django.db.models import CharField
from django.db.models import TextField

from django.db import models as models

class Dokter(models.Model) :
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 25)
    bidang = models.TextField(max_length = 255)
    jadwal_praktek = models.TextField(max_length = 255)

class Pasien(models.Model) :
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 25)
    alamat = models.TextField(max_length = 255)
    keluhan = models.TextField(max_length = 600)

class Resep(models.Model) :
    nama = models.CharField(max_length = 255)
    total_harga = models.CharField(max_length = 600)
    kumpulan_obat = models.CharField(max_length = 600)

class Obat(models.Model) :
    nama = models.CharField(max_length = 255)
    kandungan = models.TextField(max_length = 600)
    khasiat = models.CharField(max_length = 600)
    
