from django.shortcuts import render
from apps.models import *
from django.http import HttpResponse
import re

# Create your views here.


def ChaXun(request):
	if request.methond == 'POST':
		status1 = request.POST.get('status1')
		status2 = request.POST.get('status2')
		status0 = request.POST.get('status0')
		date_time = request.POST.get("date")
		#得到的时间进行切割处理
		c = re.compile(r'(\d-\d)')
		a = (c.findall(date_time))[0]
		xx = a.split('-')
		if status0 and status1 == None and status2 == None:
			data = Deal.objects.filter(status=status0).all()
			in_num = 0
			out_num = 0
			file_dict = {}
			for file in data:
				times = str(file.add_time)
				times = (times.split(' '))[0]
				time = times.split('-')
				#满足条件的进行查询输出
				if int(xx[0]) <= int(time[1]) <= int(xx[1]):
					#统计收入金额的数量
					if file.price_in != "":
						in_num += 1
						price_in = file.price_in
						file_dict["price_in"]: price_in
					#统计指出金额的数量
					if file.price_out != "":
						out_num += 0
						price_out=file.price_out
						file_dict["price_out"]: price_out
					file_dict = {
						"jiaoyifang":file.deal_id.jiao_name,
						"ka_num": file.bank_id.ka_num,
						"status":file.status,
					}
			return HttpResponse(file_dict)
		elif status0 and status1 and status2 == None:
			data = Deal.objects.filter(status=status0).all()
			in_num = 0
			out_num = 0
			file_dict = {}
			for file in data:
				times = str(file.add_time)
				times = (times.split(' '))[0]
				time = times.split('-')
				# 满足条件的进行查询输出
				if int(xx[0]) <= int(time[1]) <= int(xx[1]):
					# 统计收入金额的数量
					if file.price_in != "":
						in_num += 1
						price_in = file.price_in
						file_dict["price_in"]: price_in
					# 统计指出金额的数量
					if file.price_out != "":
						out_num += 0
						price_out = file.price_out
						file_dict["price_out"]: price_out
					file_dict = {
						"jiaoyifang": file.deal_id.jiao_name,
						"ka_num": file.bank_id.ka_num,
						"status": file.status,
					}
			return HttpResponse(file_dict)
		elif status0 and status1  and status2 :
			data = Deal.objects.filter(status__in=[status0,status1,status2]).all()
			in_num = 0
			out_num = 0
			file_dict = {}
			for file in data:
				times = str(file.add_time)
				times = (times.split(' '))[0]
				time = times.split('-')
				# 满足条件的进行查询输出
				if int(xx[0]) <= int(time[1]) <= int(xx[1]):
					# 统计收入金额的数量
					if file.price_in != "":
						in_num += 1
						price_in = file.price_in
						file_dict["price_in"]: price_in
					# 统计指出金额的数量
					if file.price_out != "":
						out_num += 0
						price_out = file.price_out
						file_dict["price_out"]: price_out
					file_dict = {
						"jiaoyifang": file.deal_id.jiao_name,
						"ka_num": file.bank_id.ka_num,
						"status": file.status,
					}

			return HttpResponse(file_dict)







