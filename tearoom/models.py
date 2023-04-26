from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique book instances


class Allergen(models.Model):
    """Model representing a food allergy."""
    allergen_name = models.CharField(max_length=200, help_text='Enter a food allergy (e.g. gluten)')
    def __str__(self):
        """String for representing the Model object."""
        return self.allergen_name


class Restaurant(models.Model):
    """Model representing restaurant"""
    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this restaurant')
    restaurant_name = models.CharField(max_length=100)
    restaurant_address = models.CharField(max_length=100)
    restaurant_city = models.CharField(max_length=100)
    restaurant_state = models.CharField(max_length=100)
    restaurant_zipcode = models.CharField("zip code", max_length=5, default="68134")
    restaurant_email = models.EmailField(max_length=254)
    restaurant_phone = models.CharField(max_length=12)


class Customer(models.Model):
    """Model representing customers."""
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this restaurant')
    customer_username = models.DateField(null=True, blank=True)
    customer_password = models.CharField(max_length=30)
    customer_first = models.CharField(max_length=100)
    customer_last = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=254)



class Review(models.Model):
    """Model representing reviews."""
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this restaurant')
    review_date = models.DateField(null=True, blank=True)
    review_time = models.CharField(max_length=100)
    review_subject = models.CharField(max_length=100)
    review_description = models.CharField(max_length=100)
    review_image = models.CharField("zip code", max_length=5, default="68134")
    restaurant_email = models.EmailField(max_length=254)
    restaurant_phone = models.CharField(max_length=12)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.RESTRICT, null=True)
    auth_user = models.ForeignKey('Customer', on_delete=models.RESTRICT, null=True)


class Employee(models.Model):
    """Model representing employees."""
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this restaurant')
    employee_first = models.CharField(max_length=100)
    employee_last = models.CharField(max_length=100)
    employee_address = models.CharField(max_length=100)
    employee_city = models.CharField(max_length=100)
    employee_state = models.CharField(max_length=100)
    employee_zipcode = models.CharField("zip code", max_length=5, default="68134")
    employee_email = models.EmailField(max_length=254)
    employee_phone = models.CharField(max_length=12)
    employee_DOB = models.DateField(null=True, blank=True)
    EMPLOYEE_TYPE = (
        ('r', 'Regular'), ('s', 'Supervisor'), ('m', 'Manager'),
    )
    employee_wage = models.DecimalField(max_digits = 5, decimal_places = 2)


class Order(models.Model):
    """Model representing orders."""
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this restaurant')
    order_date = models.DateField(null=True, blank=True)
    order_time = models.CharField(max_length=100)
    order_address = models.CharField(max_length=100)
    order_phone = models.CharField(max_length=12, default=4029999999)
    order_total = models.DecimalField(max_digits = 5, decimal_places = 2)
    menuItem = models.ForeignKey('MenuItem', on_delete=models.RESTRICT, null=True)
    auth_user = models.ForeignKey('Customer', on_delete=models.RESTRICT, null=True)
    employee = models.ForeignKey('Employee', on_delete=models.RESTRICT, null=True)



class MenuItem(models.Model):
    """Model representing menu items."""
    menu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this restaurant')
    menu_item_name = models.CharField(max_length=100)
    menu_price = models.DecimalField(max_digits = 5, decimal_places = 2)
    menu_item_description = models.CharField(max_length=100)
    menu_item_ingredients = models.CharField(max_length=100)
    menu_item_image = models.ImageField(upload_to='img/', null=True,blank=True)
    menu_is_a_Drink = models.BooleanField(default=True, help_text='Check if this is item is a drink, uncheck if it is a snack')
    allergen = models.ManyToManyField(Allergen, help_text='Select a food allergy')

    def __str__(self):
        """String for representing the Model object."""
        return self.menu_item_name

    def get_absolute_url(self):
        return reverse('menu: menu', args=[str(self.id)])

