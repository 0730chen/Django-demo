from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board

def index(request):
	
	boards = Board.objects.all()
	boards_names = list()
	print(request)
	return render(request,'index.html')
def GetAPi(request):

	return HttpResponse("哈哈")
def home(request):

    return render(request,'home.html')
