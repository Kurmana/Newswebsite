from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='news/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_date']


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_date']

