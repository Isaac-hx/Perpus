from django.db import models

# Create your models here.


#Model pada tabel kelompok pada foreignkey buku
class Kelompok(models.Model):
    nama = models.CharField(max_length=9)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama
    


#Model pada tabel buku
class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=40)
    jumlah = models.IntegerField(null=True)
    kelompok = models.ForeignKey(Kelompok,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.judul

class Karyawan(models.Model):
    nama = models.CharField(max_length=20)
    umur = models.IntegerField(null=True)

    def __str__(self):
        return self.nama
    

