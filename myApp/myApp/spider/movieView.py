from django.shortcuts import render
from django.http import HttpResponse

from .movie import run
# from movie import run

def GetMoive(request):
	date = request.GET['beginDate']
	url = 'http://piaofang.maoyan.com/second-box?beginDate='+date
	rank = run.Movie(url,50)
	res = rank.GetHtml()
	
	return HttpResponse(res)


# Create your views here.
