from django.shortcuts import render
from myfiles.models import Portfolio
# Create your views here.
def index(malumot):
    ishlarimiz = Portfolio.objects.all()
    return render(malumot,'index.html',{"works":ishlarimiz})







def portfolio(malumot,id):
    ishlarimiz = Portfolio.objects.get(id=id)
    return render(malumot , 'portfolio-details.html',{"work":ishlarimiz})




















