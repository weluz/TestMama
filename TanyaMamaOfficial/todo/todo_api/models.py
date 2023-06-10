from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    text = models.CharField(max_length = 180)
    jenis_barang = models.CharField(max_length = 180, default="", blank = True, null = True)
    harga_barang = models.CharField(max_length = 180, default="", blank = True, null = True)
    promo_value = models.CharField(max_length = 180, default="", blank = True, null = True)
    marketplace = models.CharField(max_length = 180, default="", blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task