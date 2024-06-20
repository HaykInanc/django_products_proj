from django.shortcuts import render
from django.views import View
from .models import *

class TaskView(View):

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'app/all_tasks.html', {"tasks": tasks})
    
class ProductView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'app/all_products.html', {"products": products})