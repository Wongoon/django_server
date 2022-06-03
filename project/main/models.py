from django.db import models

# Create your models here.
class Blog(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Comment(models.Model):
    subject = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField()