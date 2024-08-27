from django.db import models
from django.shortcuts import reverse

# Create your models here.
genre_choices = (
    ("classic", "Classic"),
    ("romantic", "Romantic"),
    ("comic", "Comic"),
    ("fantasy", "Fantasy"),
    ("horror", "Horror"),
    ("educational", "Educational"),
)
book_type_choices = (
    ("hardcover", "Hard cover"),
    ("ebook", "E-Book"),
    ("audiobook", "Audiobook"),
)


class Book(models.Model):
    name = models.CharField(max_length=120)
    author_name = models.CharField(max_length=120, default="Unknown Author")
    price = models.FloatField(help_text="in USdollars $", default=0.0)
    genre = models.CharField(max_length=12, choices=genre_choices, default="classic")
    book_type = models.CharField(max_length=12, choices=book_type_choices, default="hardcover")

    pic = models.ImageField(upload_to='books', default='default.jpg')
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse ('books:detail', kwargs={'pk': self.pk})
