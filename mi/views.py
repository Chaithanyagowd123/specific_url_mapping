from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit.html')

def sky(request):
    return HttpResponse('<marquee><h1>BUMRA THE GTEAT BOWLER</h1></marquee>')
