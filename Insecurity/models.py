from django.db import models

# Create your models here.
class InsecureModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    file=models.FileField()
    
    class Meta:
        db_table='InsecureModel'
    def __str__(self):
        return self.title
