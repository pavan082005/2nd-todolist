from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharFie ld(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text