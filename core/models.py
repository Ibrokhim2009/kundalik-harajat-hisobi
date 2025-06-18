from django.db import models
from core.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"({self.name} - {self.user})"
    
 
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    destriction = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.amount} - {self.category} ({self.date})"