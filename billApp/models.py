from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Enterprise(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self) -> str:
        return self.name

class Bill(models.Model):
    enterprise = models.ForeignKey(
        Enterprise,
        on_delete=models.CASCADE,
        related_name='bills'
    )
    overdue_date = models.DateTimeField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    bill_file = models.FileField(upload_to='bills/')
    notification_date = models.DateTimeField()
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Overdue", "Overdue"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")

    def __str__(self) -> str:
        return f"O boleto pertencente a {self.enterprise.name}, no valor de R${self.value}"