from django.db import models

# Create your models here.
class Website(models.Model):
    url_name      = models.CharField(max_length=100)
    total_count   = models.IntegerField()
    
    def __str__(self):
        return  str(self.url_name)