from django.db import models

# Create your models here.


class machine_hw(models.Model):
    name = models.CharField(max_length=250)
    id_machine = models.IntegerField()


class data_hg(models.Model):
    temp_1 = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    humid_1 = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    sw_1 = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    sw_2 = models.IntegerField()  # 1 generate 2 start , 4 stop , 3 finish
    machine = models.ForeignKey(
        machine_hw, related_name='machine', on_delete=models.CASCADE)
    time_data = models.DateTimeField(auto_now=True, null=True)
