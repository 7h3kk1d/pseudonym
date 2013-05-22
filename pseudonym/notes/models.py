from django.db import models

# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=30)
    visible = models.BooleanField()
    def __str__(self):
        return str(self.id)
