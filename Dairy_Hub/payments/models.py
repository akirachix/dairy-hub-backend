from django.db import models
from orderItems.models import OrderItems

# Create your models here.
class Payments(models.Model):
    order_item_id= models.ForeignKey(OrderItems,on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method=models.CharField(max_length=50)
    date_paid=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"Payment of {self.amount_paid} for Order {self.order_item_id}"