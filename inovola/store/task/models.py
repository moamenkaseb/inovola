from django.db import models

# Create your models here.

# cofee_machine db
class machine(models.Model):
    prodouct = models.CharField(max_length=50)
    modeel = models.CharField(max_length=50)
    water = models.BooleanField()

    def __str__(self):
        return f"type:{self.prodouct} and model {self.modeel} and  wate-line{self.water}"

# code
class machine_code(models.Model):
    code = models.CharField(max_length=10)
    machine_code = models.ForeignKey(machine , on_delete = models.CASCADE)

    def __str__(self):
        return f"code:{self.code} and relater-to{self.machine_code}"

# coffe_pods db

class pods(models.Model):
    prodouct = models.CharField(max_length=50)
    flavar = models.CharField(max_length=50)
    size = models.IntegerField()

    def __str__(self):
        return f"typee:{self.prodouct} and flavar:{self.flavar} and size:{self.size}"

# code
class pods_code(models.Model):
    code = models.CharField(max_length=10)
    pods_code = models.ForeignKey(pods , on_delete = models.CASCADE)

    def __str__(self):
        return f"code:{self.code} related to:{self.pods_code}"