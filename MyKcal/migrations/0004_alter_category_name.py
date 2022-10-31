# Generated by Django 4.1.2 on 2022-10-31 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyKcal', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Baked Foods', 'Baked Foods'), ('Snacks', 'Snacks'), ('Sweets', 'Sweets'), ('Vegetables', 'Vegetables'), ('American India', 'American Indian'), ('Restaurant Foods', 'Restaurant Foods'), ('Beverages', 'Beverages'), ('Fats and Oils', 'Fats and Oils'), ('Meats', 'Meats'), ('Dairy and Egg Products', 'Dairy and Egg Products'), ('Baby Foods', 'Baby Foods'), ('Breakfast Cereals', 'Breakfast Cereals'), ('Soups and Sauces', 'Soups and Sauces'), ('Soups and Sauces', 'Soups and Sauces'), ('Fish', 'Fish'), ('Fruits', 'Fruits'), ('Grains and Pasta', 'Grains and Pasta'), ('Nuts and Seeds', 'Nuts and Seeds'), ('Fast Foods', 'Fast Foods'), ('Spices and Herbs', 'Spices and Herbs'), ('Prepared Meals', 'Prepared Meals')], max_length=50),
        ),
    ]
