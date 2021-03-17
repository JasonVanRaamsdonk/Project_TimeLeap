from django.shortcuts import render
from django.http import HttpResponse
from time_leap.models import Topic, Webpage, AccessRecord, Colourise
from .colorization.demo_timeleap import convert_img

# Create your views here.

def index(request):
    # print(request.FILES['image_input'])

    image_list = Colourise.objects.all()
    image_dict = {'image_uploads': image_list, 'flag':False}
    if request.method == "POST":
        img = request.FILES['image_input']
        img_size = convert_img(img)
        image_dict = {'image_uploads':None, 'img_size':img_size, 'flag':True}

    # webpages_list = AccessRecord.objects.order_by('date')
    # date_dict = {'access_records': webpages_list}

    # image_list = Colourise.objects.all()
    # image_dict = {'image_uploads': None}

    # my_dict = {'insert_me' : "Now I am coming from time_leap/index.html!"}
    # return render(request, 'time_leap/index.html', context=my_dict)

    # return render(request, 'time_leap/index.html', context=date_dict)
    return render(request, 'time_leap/index.html', context=image_dict)
