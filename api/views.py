from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import StudentSerializer
from api.models import Student
# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def home(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data is successfully save in database.'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data successfully updated.'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'message': 'Data successfully deleted.'})
@api_view()
def getdata(request, id):
    stu = Student.objects.get(id=id)
    serializer = StudentSerializer(stu)
    return Response(serializer.data)
