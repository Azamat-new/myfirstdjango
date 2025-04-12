from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.title}, {self.publication_date}"
