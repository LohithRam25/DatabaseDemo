from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.
def response(request):
  stu=Student.objects.all()
  for st in stu:
    print(st.sname)

  return HttpResponse("Avuthundi le")