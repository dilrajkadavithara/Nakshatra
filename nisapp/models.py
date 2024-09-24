from django.core.validators import RegexValidator
from django.db import models

class District(models.Model):
    district_id = models.CharField(max_length=10, primary_key=True)  # Alphanumeric ID
    district_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.district_name

class LocalArea(models.Model):
    local_area_id = models.CharField(max_length=10, primary_key=True)  # Alphanumeric ID
    local_area_name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.local_area_name

class Lead(models.Model):
    lead_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Phone number must be exactly 10 digits.',
            ),
        ],
    )
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    local_area = models.ForeignKey(LocalArea, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"