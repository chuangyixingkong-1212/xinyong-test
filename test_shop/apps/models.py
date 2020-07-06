
#coding=gbk
from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=20)

	class Meta:
		db_table = 'df_user'

class JiaoYi(models.Model):
	jiao_name = models.CharField(max_length=100,null=True)

	class Meta:
		db_table = "df_jiaoyi_user"

class Bank(models.Model):
	ka_num = models.IntegerField(max_length=20)
	user_id = models.ForeignKey('User',on_delete=models.CASCADE)
	money = models.FloatField()


	class Meta:
		db_table = "df_bank"

class Deal(models.Model):
	status_choices = (
		(0, "待检查"),
		(1, "有风险"),
		(2, "无风险")
	)

	status = models.SmallIntegerField(default=0, choices=status_choices)
	price_in =models.DecimalField(max_digits=10, decimal_places=2)
	price_out =models.DecimalField(max_digits=10, decimal_places=2)
	bank_id = models.ForeignKey('Bank',on_delete=models.CASCADE)
	deal_id = models.ForeignKey("JiaoYi",on_delete=models.CASCADE)
	add_time = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "df_detail"

