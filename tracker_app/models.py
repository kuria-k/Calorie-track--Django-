from django.db import models

class FoodItem(models.Model):
    MEAL_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]

    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    meal_type = models.CharField(max_length=10, choices=MEAL_CHOICES)
    date = models.DateField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.calories} cal)"

