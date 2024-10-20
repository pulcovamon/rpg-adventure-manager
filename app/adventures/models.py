from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    hashed_password = models.CharField(max_length=30)


class Adventure(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, blank=True)
    start_level = models.IntegerField(null=True)
    estimated_end_level = models.IntegerField(null=True)
    estimated_duration = models.DurationField(null=True)
    
    
class Event(models.Model):
    adventure_id = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, blank=True)
    expected_level = models.IntegerField(null=True)