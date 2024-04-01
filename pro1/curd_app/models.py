from django.db import models


class Pan(models.Model):
    mar = [("SINGLE", "single"), ("MARRIED", "married"), ("DIVORCE", "divorce"), ("WIDOW", "widow")]
    gen = [("WOMEN", "women"), ("MEN", "men"), ("OTHER", "other"), ("GIRL", "girl"), ("BOY", "boy")]
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=gen, default=True)
    phone = models.IntegerField()
    dob = models.DateField()
    marital_status = models.CharField(max_length=10, choices=mar, default=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

