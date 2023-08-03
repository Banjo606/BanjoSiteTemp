from django.contrib import admin
from django.db import models

# Create your models here.
class lottery_539(models.Model):
    drawdate = models.DateField()
    num_1 = models.SmallIntegerField()
    num_2 = models.SmallIntegerField()
    num_3 = models.SmallIntegerField()
    num_4 = models.SmallIntegerField()
    num_5 = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

@admin.register(lottery_539)
class lottery_539_Admin(admin.ModelAdmin):
    # 這裡我一併將 Vendor 類別 其它的欄位都加進來了
	list_display = ['id', 'drawdate', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5']