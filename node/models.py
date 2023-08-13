from django.db import models

# Create your models here.


class water_tank(models.Model):
    rms = models.CharField(max_length=300,blank=True,null=True)
    pump_status = models.CharField(max_length=300,blank=True,null=True)
    cumulative_lpd = models.CharField(max_length=300,blank=True,null=True)
    current_lpm = models.CharField(max_length=300,blank=True,null=True)
    voltage = models.CharField(max_length=300,blank=True,null=True)
    current = models.CharField(max_length=300,blank=True,null=True)
    power = models.CharField(max_length=300,blank=True,null=True)
    location = models.CharField(max_length=300,blank=True,null=True)
    district = models.CharField(max_length=300,blank=True,null=True)
    size_of_the_system = models.CharField(max_length=300,blank=True,null=True)
    contractor_name = models.CharField(max_length=300,blank=True,null=True)
    contractor_number = models.CharField(max_length=300,blank=True,null=True)
    serial_numbers = models.CharField(max_length=300,blank=True,null=True)
    wattage = models.CharField(max_length=300,blank=True,null=True)
    no_of_panels = models.CharField(max_length=300,blank=True,null=True)
    installation_date = models.CharField(max_length=300,blank=True,null=True)
    capacity = models.CharField(max_length=300,blank=True,null=True)
    imei = models.CharField(max_length=300,blank=True,null=True)
    ratings = models.CharField(max_length=300,blank=True,null=True)
    model_number = models.CharField(max_length=300,blank=True,null=True)
    fault = models.CharField(max_length=300,blank=True,null=True)
    reported_on = models.CharField(max_length=300,blank=True,null=True)
    attended_on = models.CharField(max_length=300,blank=True,null=True)
    current_status = models.CharField(max_length=300,blank=True,null=True)
    remarks = models.CharField(max_length=300,blank=True,null=True)
    start_time = models.CharField(max_length=300,blank=True,null=True)
    stop_time = models.CharField(max_length=300,blank=True,null=True)
    run_time_today = models.CharField(max_length=300,blank=True,null=True)





class water_tank_times(models.Model):
    rms = models.CharField(max_length=300,blank=True,null=True)
    
