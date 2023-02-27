from django.db import models

TITLE_CHOICES = [
    ("MR", "Mr."),
    ("MRS", "Mrs."),
    ("MS", "Ms."),
]


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    def get_authors(self):
        return "\n".join([p.name for p in self.authors.all()])
