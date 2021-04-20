from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
