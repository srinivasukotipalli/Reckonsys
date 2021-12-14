from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

    def __str__(self):
        return str(self.pk)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.TextField()

    def __str__(self):
        return self.title
