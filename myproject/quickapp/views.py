from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
@api_view(['POST'])
def getdata(request):
    print(request.data)
    username=request.data.get('name')
    password=request.data.get('password')
    new_student=student(username=username,password=password)
    new_student.save()
    return Response('new data created')
@api_view(['POST'])
def createid(request):
    print(request.data)
    username=request.data.get('name')
    new_id = roomid.objects.create(username=username)
    new_id.save()
    domain='https://quickmeet.inoesis.com/'
    profile_url=f"{domain}{username}"
    return Response(profile_url)
   
@api_view(['POST'])
def createname(request):
    print(request.data)
    username=request.data.get('username')
    newname=roomname.objects.create(username=username)
    newname.save()
    domain='https://quickmeet.inoesis.com/'
    profile_url=f"{domain}{username}"
    return Response(profile_url)
# Create your views here.
