from django.shortcuts import render
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def studentview(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")

    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        print("Stream",stream)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            dict={"msg":"Student Created Successfully."}
            pythondata=JSONRenderer().render(dict)
            return HttpResponse(pythondata,content_type="applicaton/json")

        pythondata=JSONRenderer().render(serializer.errors)
        return HttpResponse(pythondata,content_type="application/json")
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        #print("updated data",pythondata)
        id=pythondata.get('id')
        #print("id",id)
        stu=Student.objects.get(id=id)
        #print("original data",stu)
        #print("original data",stu)
        serializer=StudentSerializer(stu,data=pythondata)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            json_data=JSONRenderer().render({"msg":"data updated"})
            return HttpResponse(json_data,content_type="application/json")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondict=JSONParser().parse(stream)
        id=pythondict.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        dict={"msg":"Student deleted Successfully!!"}
        json_data=JSONRenderer().render(dict)
        return HttpResponse(json_data,content_type="application/json")
