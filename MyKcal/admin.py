from django.contrib import admin
from .models import Activity, Category, UserProfile, Food

# Register your models here.
admin.site.register(Activity)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Food)
