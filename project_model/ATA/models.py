from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateTimeField
from django.utils import timezone

from django.db import models as models

class Mata_Pelajaran(models.Model) :
    nama_pelajaran = models.CharField(max_length = 25)
    jadwal_dimulai = models.DateTimeField()
    jadwal_berakhir = models.DateTimeField()

    def __str__(self) :
        return self.nama_pelajaran

class Direksi(models.Model) :
    nama_lengkap = models.CharField(max_length =255)
    nomor_telepon = models.CharField(max_length = 25)
    jabatan = models.TextField(max_length = 55)

class Mentee(models.Model) :
    nama_lengkap = models.CharField(max_length =255)
    nomor_telepon = models.CharField(max_length = 25)
    nomor_absen = models.CharField(max_length = 5)
    nilai_rata_rata = models.CharField(max_length = 10)

class Mentor(models.Model) :
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 25)
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete = models.CASCADE)

class Challenge(models.Model) :
    nama_challenge = models.CharField(max_length = 55)
    banyak_soal = models.CharField(max_length = 5)
    bobot_nilai = models.CharField(max_length = 15)
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete = models.CASCADE)

class Live_Code(models.Model) :
    nama_live_code = models.CharField(max_length = 55)
    banyak_soal = models.CharField(max_length = 5)
    bobot_nilai = models.CharField(max_length = 15)
    tanggal_pelaksanaan = models.DateTimeField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete = models.CASCADE)
