from django.core import paginator
from django.http import request, response
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
import pandas as pd
from .utils.mongo_setup import *
from django.core.paginator import Paginator
from datetime import datetime
from datetime import timedelta
from bson import ObjectId


# Create your views here.

def index(request):
    x = collection.find({},{"city_id":"Hassan"})
    file =('Sample upcoming events in _ Rome - Barcelona.xlsx')
    newData = pd.read_excel(file,sheet_name="Bangalore")
    ctx = {
        "data":newData
    }

    return render(request,'base/eventsScreen.html',ctx)


def eventsView(request):
    pass


def hotels(request):
    hotel_names = collection.find({}, {'name':1, '_id':1})
    hotels = []
    for hotel in hotel_names:
        hotels.append(hotel)
    return render(request,'base/hotels.html',{"hotels":hotels})


def hotelinfo(request):
    if request.method == "POST":
        id = request.POST.get('id')
        obj_id = ObjectId(id)
        hotel = collection.find_one({"_id":obj_id})
        # print(hotel)
        file =('Sample upcoming events in _ Rome - Barcelona.xlsx')
        newData = pd.read_excel(file,sheet_name=hotel["city_id"])
        return render(request,"base/hotelinfo.html",{"id":id,"events":newData,"hotelData":hotel})
    



def increaseroomprice(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        event_name = data.get("name")
        hotel_id = data.get("hotelId")
        print(hotel_id)
        from_date = data.get("start")
        to_date = data.get("end")
        increase = data.get("increase")
        obj_id = ObjectId(hotel_id)

        mongo_data = [
            {
                "Name":event_name,
                "start_date":from_date,
                "end_date":to_date,
                "increase_percentage":increase
            }
        ]
        collection.update(
        {"_id":obj_id},
        {"$addToSet":{"events":mongo_data}}
        )
        file =('Sample upcoming events in _ Rome - Barcelona.xlsx')
        newData = pd.read_excel(file,sheet_name="Bangalore")
        hotel = collection.find_one({"_id":obj_id})
        return render(request,"base/hotelinfo.html",{"id":id,"events":newData,"hotelData":hotel,"success":"success"})
