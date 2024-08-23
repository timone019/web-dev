from django.db import models

# Create your models here.

from books.models import Book 
#because we need to connect sales with books
class Sale(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE) 
    quantity=models.PositiveIntegerField()
    price = models.FloatField()
    date_created = models.DateTimeField(blank=True)

    def __str__(self):
        return f"id: {self.id}, book: {self.book.name}, quantity: {self.quantity}"