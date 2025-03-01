from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    message = """
<h1>Welcome to My Django App on Vercel!</h1><br>Project/Product Management System. v1.
<br>
This is an open-source software based on MIT license.
check1
"""
    return HttpResponse(f"{message}")
