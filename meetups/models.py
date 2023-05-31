from django.db import models

# Create your models here.
               # accesses from Model base class
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'
           

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organiser_email = models.EmailField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images')
    location_of_meetup = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)
    
    

    def __str__(self):
        return f'{self.title} - {self.slug}'
    

