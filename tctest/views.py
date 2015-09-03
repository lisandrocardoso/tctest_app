from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def tctest(request):
  return HttpResponse("Terraform/Chef test app")

