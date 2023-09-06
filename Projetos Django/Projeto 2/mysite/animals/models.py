from django.db import models

# Create your models here.
class habitat(models.Model):
    Region_Name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,default="Nenhuma descrição foi adicionada")
    

    def __str__(self):
        return self.Region_Name

class animal(models.Model):
    specie_name = models.CharField(max_length=200)
    habitat = models.ForeignKey(habitat, on_delete=models.CASCADE, default=1)
    animal_image = models.ImageField(upload_to="images")
    votes = models.IntegerField(default=0)
    Animal_description = models.CharField(max_length=1000, default="")
    def __str__(self):
        return self.specie_name
    
    