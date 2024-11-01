from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import Topic, Webpage, AccesRecord

# Create your views here.
def index(request): #Penamaan Argumen Bebas
    webpages_list = AccesRecord.objects.order_by('date')
    date_dict = {'access_record': webpages_list}
    # my_dic = {'insert_me' : "Hallo django first_app/index views nich unch unch"}
    return render(request, 'first_app/index.html', context=date_dict)
