from django.db import models

# Create your models here.


class machine_hw(models.Model):
    name = models.CharField(max_length=250)
    id_machine = models.IntegerField()


class data_hg(models.Model):
    temp_1 = models.FloatField()  # 1 generate 2 start , 4 stop , 3 finish
    humid_1 = models.FloatField()  # 1 generate 2 start , 4 stop , 3 finish
    sw_1 = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    sw_2 = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    machine = models.ForeignKey(
        machine_hw, related_name='machine', on_delete=models.CASCADE)
    time_data = models.DateTimeField(auto_now=True, null=True)


class data_hg_outputs(models.Model):
    Bomba_1 = models.BooleanField()  # 1 generate 2 start , 4 stop , 3 finish
    Bomba_2 = models.BooleanField()  # 1 generate 2 start , 4 stop , 3 finish
    Bomba_3 = models.BooleanField()  # 1 generate 2 start , 4 stop , 3 finish
    Llum = models.BooleanField()  # 1 generate 2 start , 4 stop , 3 finish
    Bomba_h20 = models.BooleanField()  # 1 generate 2 start , 4 stop , 3 finish
    Ventilador = models.BooleanField()  # 1 generate 2 start , 4 stop , 3 finish
    Altura = models.IntegerField()
    machine = models.ForeignKey(
        machine_hw, related_name='machine_output', on_delete=models.CASCADE)
    time_data = models.DateTimeField(auto_now=True, null=True)


class data_hg_confgi(models.Model):
    Light_time = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    Light_on = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    H20_duty = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    Max_temp = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    Fan_Duty = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    machine = models.ForeignKey(
        machine_hw, related_name='machine_config', on_delete=models.CASCADE)
    time_data = models.DateTimeField(auto_now=True, null=True)