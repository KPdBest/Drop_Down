from django.shortcuts import render
#kkkk
from django.http import Http404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from Select.models import Cou,Bran,Semes,Sec

def show(request):
	# if request.method == 'POST' :
	# 	data = json.loads(request.body)
	# 	obj=Cou.objects.all()
	# 	for x in obj:
	# 		query=Cou.objects.filter(course=data['course']).values('id')
	# 		query2=Bran.objects.filter(link=query[0]['id']).values('branch')
	# 		print(query2)
	# 		return JsonResponse(list(query2),safe=False)
	if request.method == 'GET' :

		cou=request.GET.get('CD','1')
		bran=request.GET.get('BD','1')
		rep=request.GET.get('ID','1')


		if(cou=='1' and bran=='1'):
			q=Cou.objects.filter().values('course')
			print(q)
			return JsonResponse(list(q),safe=False)


		elif(cou!='1' and bran=='1'):
			q1=Cou.objects.filter(course=cou).values('id')
			q2=Bran.objects.filter(linkA=q1[0]['id']).values('branch','linkA__id')
			print(q2)
			return JsonResponse(list(q2),safe=False)

		elif(cou=='1' and bran!='1'):
			q3=Bran.objects.filter(branch=bran , linkA=rep).values('id') 
			q4=Semes.objects.filter(linkB=q3[0]['id']).values('semester')
			print(q4)
			return JsonResponse(list(q4),safe=False)
