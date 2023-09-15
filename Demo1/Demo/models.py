from django.db import models

class Demo(models.Model):
    STT = models.CharField(max_length=30)
    Ten_cot = models.CharField(max_length=200)
    Kieu_du_lieu = models.CharField(max_length=300)
    Chu_thich = models.CharField(max_length=300)

    class Meta:
        db_table = 'Demo'
