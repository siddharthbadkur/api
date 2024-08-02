from django.shortcuts import render
from .models import *
from .serializers import *
from  django.http import JsonResponse,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.parsers import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view 

import io
@csrf_exempt
#------------by httpresponse--------------------

# Create your views here.
# def stu_info(request):
#     data=Studentapi.objects.all()
#     serializers=studentSerializer(data,many=True)
#     jsondata=JSONRenderer().render(serializers.data)
#     return HttpResponse(jsondata,content_type='application/json')
   

# def stu_detail(request,pk):
#     data=Studentapi.objects.get(id=pk)
#     serializers=studentSerializer(data)
#     jsondata=JSONRenderer().render(serializers.data)
#     return HttpResponse(jsondata,content_type='application/json')
    

#--------------by jsonresponse-------------------
# def stu_info(request):
#     stu=Studentapi.objects.all()
#     serializers(stu,many=True)
#     return JsonResponse (serializers.data,safe=True)

# def stu_details(request,pk):
#     t=Studentapi.objects.get(id=pk)
#     serializers=studentSerializer(t)
#     jsondata=JSONRenderer().render(serializers.data)
#     return JsonResponse(jsondata,safe=True)


  
# def userList(request): 
#     if request.method =="GET":
#         user = Studentapi.objects.all()
#         serializer_data = Studentserializer(user,many=True)
#         json_data = JSONRenderer().render(serializer_data.data)
#         return HttpResponse(json_data,content_type = 'application/json')
    
#     elif request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = Studentserializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

# @csrf_exempt
# def userDetails(request,pk):
#     if request.method=='GET':
#         # id = Studentapi.objects.filter(id=pk)
#         id = Studentapi.objects.get(id=pk)
#         if id:
#             stu = Studentapi.objects.get(id=pk)
#             serializer_data = Studentserializer(stu)
#             json_data = JSONRenderer().render(serializer_data.data)
#             return HttpResponse(json_data,content_type = 'application/json')
#         else:
#             res = {'msg': 'id not present in Database'}
#             return JsonResponse(res)
    
#     elif request.method == 'PUT':
#         id = Studentapi.objects.get(id=pk)
#         if id:
#             json_data = request.body
#             stream = io.BytesIO(json_data)
#             python_data = JSONParser().parse(stream)
#             stu = Studentapi.objects.get(id=pk)
#             serializer = Studentserializer(stu, data=python_data, partial = True)
#             # serializer = UserSerializer(stu, data=python_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {'msg':'Data Updated !!'}
#                 json_data = JSONRenderer().render(res)
#                 return HttpResponse(json_data, content_type='application/json')
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             res = {'msg': 'id not present in Database'}
#             return JsonResponse(res)
    
#     elif request.method == 'PATCH':
#         id = Studentapi.objects.get(id=pk)
#         if id:
#             json_data = request.body
#             stream = io.BytesIO(json_data)
#             python_data = JSONParser().parse(stream)
#             stu = Studentapi.objects.get(id=pk)
#             serializer =Studentserializer(stu, data=python_data, partial = True)
#             # serializer = UserSerializer(stu, data=python_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {'msg':'Data Partially Updated !!'}
#                 json_data = JSONRenderer().render(res)
#                 return HttpResponse(json_data, content_type='application/json')
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             res = {'msg': 'id not present in Database'}
#             return JsonResponse(res)

#     elif request.method == 'DELETE':
#         id = Studentapi.objects.get(id=pk)
#         if id:
#             id.delete()
#             res = {'msg': 'Data Deleted!!'}
#             return JsonResponse(res, safe=False)
#         else:
#             res = {'msg': 'id not present in Database'}
#             return JsonResponse(res)

#function based api
@api_view(['GET', 'POST'])  
def movie_list(request): 
    if request.method=='GET':
        movies = Studentapi.objects.all() 
        serializer=Studentserializer(movies,many=True)
        return Response(serializer.data) 
    
    elif request.method=='POST':
        serializer=Studentserializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)

@api_view(['GET', 'PUT','DELETE']) 
def movie_details(request,pk):
    id = Studentapi.objects.get(pk=pk)
    if id:
        if request.method=='GET': 
            movie=Studentapi.objects.get(pk=pk) 
            serializer = Studentserializer(movie) 
            return Response(serializer.data) 
        
        elif request.method=='PUT': 
            movie=Studentapi.objects.get(pk=pk) 
            serializer = Studentserializer(movie,data=request.data,partial=True) 
            if serializer.is_valid(): 
                serializer.save() 
                return Response(serializer.data) 
            else: return Response(serializer.errors) 
        
        elif request.method=='PATCH': 
            movie=Studentapi.objects.get(pk=pk) 
            serializer = Studentserializer(movie,data=request.data,partial=True) 
            if serializer.is_valid(): 
                serializer.save() 
                return Response(serializer.data) 
            else: return Response(serializer.errors) 
        elif request.method=='DELETE': 
                movie=Studentapi.objects.get(pk=pk) 
                movie.delete() 
                return Response({'msg':"Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    else:
        res = {'msg': 'id not present in Database'}
        return Response(res)
     

    








def list(request):
    if request.method =="GET":
        user =  Studentapi.objects.all()
        serializer_data = Studentserializer(user,many=True)
        # print(serializer_data.data)
        json_data = JSONRenderer().render(serializer_data.data)
        return HttpResponse(json_data,content_type = 'application/json')
    
    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data) 
        python_data = JSONParser().parse(stream)
        serializer = Studentserializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    elif request.method=='PUT':
         

        json_data = request.body
        stream = io.BytesIO(json_data) 
        python_data = JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Studentapi.objects.get(id=id)
        serializer = Studentserializer(stu,data = python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    elif request.method == 'DELETE':   
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id:
            stu = Studentapi.objects.get(id=id)
            stu.delete()
            res = {'msg': 'Data Deleted!!'}
            return JsonResponse(res, safe=False)
        else:
            res = {'msg': 'id not present in Database'}
        return JsonResponse(res)

 
  