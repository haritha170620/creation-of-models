from django.db import models

# Create your models here.
class Country(models.Model):
    country_id=models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=100)
    country_language=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.country_id
        return self.country_name
        return self.country_language
    
class Capital(models.Model):
    capital_id=models.IntegerField(primary_key=True)
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)
    capital_name=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.capital_id
        return self.capital_name
    


    