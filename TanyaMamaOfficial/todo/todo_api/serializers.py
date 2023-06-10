from rest_framework import serializers
from .models import Todo
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["text", "jenis_barang", "harga_barang", "promo_value", "marketplace", "user"]