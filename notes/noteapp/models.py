from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    nametag = models.CharField(max_length=25, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'nametag'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.nametag}"
    
class Author_note(models.Model):
    fullname = models.CharField(max_length=250, null=False)
    born_date = models.DateTimeField()
    born_location = models.CharField(max_length=250, null=False)
    description = models.CharField(max_length=250, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f"{self.fullname}"


class Note(models.Model):
    description = models.CharField(max_length=150, null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField(Author_note)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.description}"
    

