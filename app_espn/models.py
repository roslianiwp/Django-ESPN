from django.db import models
from datetime import datetime

# Create your models here.
class Kategori(models.Model):
    kategori_artikel = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.kategori_artikel}"

class UserNetijen(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_user = models.CharField(max_length=50, null=True)
    profile_pic = models.ImageField(upload_to='',blank=True)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.username}"

class UserWartawan(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_user = models.CharField(max_length=50, null=True)
    profile_pic = models.ImageField(upload_to='',blank=True)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.username}"

class Artikel(models.Model):
    published_date = models.DateTimeField(default=datetime.now(), blank=True)
    judul = models.CharField(max_length=500)
    author = models.ForeignKey(UserWartawan, on_delete=models.CASCADE)
    kategori_artikel= models.ForeignKey(Kategori, on_delete=models.CASCADE)
    gambar = models.FileField(upload_to='')
    konten = models.TextField()
    clap = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.judul}"

class Komen(models.Model):
    tgl_komen = models.DateTimeField(default=datetime.now(), blank=True)
    artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)
    netizen = models.ForeignKey(UserNetijen, on_delete=models.CASCADE)
    komen = models.TextField()

    def __str__(self):
        return f"{self.artikel}"

class Like(models.Model):
    tgl_like = models.DateTimeField(default=datetime.now(), blank=True)
    artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)
    netizen = models.ForeignKey(UserNetijen, on_delete=models.CASCADE)
    like_artikel = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.artikel}"