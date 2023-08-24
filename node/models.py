from django.db import models

# Create your models here.


class water_tank(models.Model):
    rms = models.CharField(max_length=300,blank=True,null=True)
    pump_status = models.CharField(max_length=300,blank=True,null=True)
    location = models.CharField(max_length=300,blank=True,null=True)
    district = models.CharField(max_length=300,blank=True,null=True)
    state = models.CharField(max_length=300,blank=True,null=True)
    contractor_name = models.CharField(max_length=300,blank=True,null=True)
    contractor_number = models.CharField(max_length=300,blank=True,null=True)
    installation_date = models.CharField(max_length=300,blank=True,null=True)
    capacity = models.CharField(max_length=300,blank=True,null=True)

    pump_serial_numbers = models.CharField(max_length=300,blank=True,null=True)
    pump_model_number = models.CharField(max_length=300,blank=True,null=True)
    controller_model_number = models.CharField(max_length=300,blank=True,null=True)
    controller_serial_numbers = models.CharField(max_length=300,blank=True,null=True)

    modem_id = models.CharField(max_length=300,blank=True,null=True)
    sim_id = models.CharField(max_length=300,blank=True,null=True)
    iccid = models.CharField(max_length=300,blank=True,null=True)

    start_time = models.TimeField(blank=True,null=True)
    stop_time = models.TimeField(max_length=300,blank=True,null=True)
    benificery_name = models.CharField(max_length=300,blank=True,null=True)
    signal_strength = models.CharField(max_length=300,blank=True,null=True)
    make = models.CharField(max_length=300,blank=True,null=True)
    site_address = models.CharField(max_length=300,blank=True,null=True)
    created_by = models.CharField(max_length=300,blank=True,null=True)
    
    # imei = models.CharField(max_length=300,blank=True,null=True)
    # ratings = models.CharField(max_length=300,blank=True,null=True)
    # no_of_panels = models.CharField(max_length=300,blank=True,null=True)
    # size_of_the_system = models.CharField(max_length=300,blank=True,null=True)
    # fault = models.CharField(max_length=300,blank=True,null=True)
    # reported_on = models.CharField(max_length=300,blank=True,null=True)
    # attended_on = models.CharField(max_length=300,blank=True,null=True)
    # current_status = models.CharField(max_length=300,blank=True,null=True)
    # remarks = models.CharField(max_length=300,blank=True,null=True)






class water_tank_records(models.Model):
    rms = models.CharField(max_length=300,blank=True,null=True)
    cumulative_lpd = models.FloatField(max_length=300,blank=True,null=True)
    current_lpm = models.FloatField(max_length=300,blank=True,null=True)
    voltage = models.FloatField(max_length=300,blank=True,null=True)
    current = models.FloatField(max_length=300,blank=True,null=True)
    power = models.FloatField(max_length=300,blank=True,null=True)
    wattage = models.FloatField(max_length=300,blank=True,null=True)
    present_lpm = models.FloatField(max_length=300,blank=True,null=True)
    start_time = models.TimeField(blank=True,null=True)
    stop_time = models.TimeField(max_length=300,blank=True,null=True)
    signal_strength = models.CharField(max_length=300,blank=True,null=True)
    run_time_today = models.CharField(max_length=300,blank=True,null=True)
    time = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True)


class water_tank_records_temp(models.Model):
    rms = models.CharField(max_length=300,blank=True,null=True)
    cumulative_lpd = models.FloatField(max_length=300,blank=True,null=True)
    current_lpm = models.FloatField(max_length=300,blank=True,null=True)
    voltage = models.FloatField(max_length=300,blank=True,null=True)
    current = models.FloatField(max_length=300,blank=True,null=True)
    power = models.FloatField(max_length=300,blank=True,null=True)
    wattage = models.FloatField(max_length=300,blank=True,null=True)
    present_lpm = models.FloatField(max_length=300,blank=True,null=True)
    start_time = models.TimeField(blank=True,null=True)
    stop_time = models.TimeField(max_length=300,blank=True,null=True)
    run_time_today = models.CharField(max_length=300,blank=True,null=True)
    signal_strength = models.CharField(max_length=300,blank=True,null=True)
    time = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,editable=True)
