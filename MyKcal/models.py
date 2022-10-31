from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    ACTIVITIES_CHOICES=(
      ('Sedentary (Office Job, ...)','Sedentary (Office Job, ...)'),
      ('Light Exercise (1-3 days/week)','Light Exercise (1-3 days/week)'),
      ('Moderate Exercise (4-5 days/week)','Moderate Exercise (4-5 days/week)'),
      ('Heavy Exercise (6-7 days/week)','Heavy Exercise (6-7 days/week)'),
      ('Athlete (2x per day)','Athlete (2x per day)'),
    )
    name=models.CharField(max_length=50, choices=ACTIVITIES_CHOICES)
    score=models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    GENDER_CHOICES = (
      ('Male', 'Male'),
      ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age=models.IntegerField()
    weight=models.IntegerField()
    height=models.IntegerField()
    activity=models.ForeignKey(Activity, on_delete=models.CASCADE)
    calories=models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.user.username)

class Category(models.Model):
    CATEGORY_OPTIONS = (
        ('Baked Foods','Baked Foods'),
        ('Snacks','Snacks'),
        ('Sweets','Sweets'),
        ('Vegetables','Vegetables'),
        ('American India','American Indian'),
        ('Restaurant Foods','Restaurant Foods'),
        ('Beverages','Beverages'),
        ('Fats and Oils','Fats and Oils'),
        ('Meats','Meats'),
        ('Dairy and Egg Products','Dairy and Egg Products'),
        ('Baby Foods','Baby Foods'),
        ('Breakfast Cereals','Breakfast Cereals'),
        ('Soups and Sauces','Soups and Sauces'),
        ('Beans and Lentils','Beans and Lentils'),
        ('Fish','Fish'),
        ('Fruits','Fruits'),
        ('Grains and Pasta','Grains and Pasta'),
        ('Nuts and Seeds','Nuts and Seeds'),
        ('Fast Foods','Fast Foods'),
        ('Spices and Herbs','Spices and Herbs'),
        ('Prepared Meals','Prepared Meals'),
    )
    name=models.CharField(max_length=50, choices=CATEGORY_OPTIONS)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    calories=models.IntegerField()
    fat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)
