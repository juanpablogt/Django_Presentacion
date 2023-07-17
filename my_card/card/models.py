from django.db import models
class Card(models.Model):
    # Campos del modelo
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"datos de la persona: {self.name}  {self.email} {self.phone}, {self.address}"
