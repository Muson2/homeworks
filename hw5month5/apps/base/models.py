from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=155, verbose_name='Автор')
    birht_year = models.IntegerField(verbose_name='Дата рождения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'     

class Book(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    year = models.IntegerField(verbose_name='Год')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
