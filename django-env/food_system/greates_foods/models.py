from django.db import models

class town(models.Model):
    town_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.town_name}"

class foods(models.Model):
    name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)
    Town = models.ForeignKey(town, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
