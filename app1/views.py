from django.shortcuts import render
from django.http import HttpResponse
app_name = "app1"
mod_name = ""
def home(request):
    message = "test"
    context = {
        'page': 'home',
        'page_title': 'Home Page'
    }
    template_file_url = f"{app_name}/home/home.html"
    return render(request, template_file_url, context)
