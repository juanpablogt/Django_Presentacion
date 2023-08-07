from django.db import models
class Card(models.Model):
    # Campos del modelo
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mensaje = models.CharField(max_length=800)

    def __str__(self):
        return f"datos de la persona: {self.name}  {self.email} {self.mensaje}"
