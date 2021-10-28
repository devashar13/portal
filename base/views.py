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
        newData = pd.read_excel(file,sheet_name="Bangalore")
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
        # collection.update(
        # {"_id":obj_id},
        # {"$addToSet":{"events":mongo_data}}
        # )
        file =('Sample upcoming events in _ Rome - Barcelona.xlsx')
        newData = pd.read_excel(file,sheet_name="Bangalore")
        find = collection.find({"_id":obj_id},{"mappings.channel_manager.rate_plans_rate_type":1})
    
        # print(find)
        # find = collection.find(
        #     {"_id":obj_id},{"_id":1,"mappings.channel_manager.rate_plans_rate_type":1})
        inc  = 1 + float(float(increase)/float(100))
        rate_type_list = []
        for ho in find:
            hotel_info = ho

        rate_plans_rate_type = hotel_info['mappings']['channel_manager']['rate_plans_rate_type'].keys()

        for rate_plans in rate_plans_rate_type:
            print(rate_plans)
            for x in hotel_info['mappings']['channel_manager']['rate_plans_rate_type'][rate_plans]['rate_plan_list'].keys():

                mapped_name = hotel_info['mappings']['channel_manager']['rate_plans_rate_type'][rate_plans]['rate_plan_list'][x]["mapped_name"]
            
            for i,name in enumerate(mapped_name):
                collection.update(
                    {"_id":obj_id},
                    {"$mul":{"mappings.channel_manager.rate_plans_rate_type.{}.rate_plan_list.{}.mapped_name.{}.price".format(rate_plans,x,i):inc}
                    },multi=True)
            

        


            
            # z = rate['mappings']['channel_manager']['rate_plans_rate_type']
            




        # hotel = collection.update(
        #     {"_id":obj_id},{"$mul":{"price":1.05}},multi=True)
        # for ho in hotel:
        #     print(ho)

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
        hotel = collection.find_one({"_id":obj_id})

        return render(request,"base/hotelinfo.html",{"id":id,"events":newData,"hotelData":hotel,"success":"success"})

