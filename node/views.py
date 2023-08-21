from django.shortcuts import render ,redirect
from .models import *
from .Serializers import *
from rest_framework.permissions import IsAuthenticated
from braces.views import GroupRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import HttpResponse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.core.cache import cache

import json






# Create your views here.


class get_all_data(APIView):
    permission_classes = (IsAuthenticated, )
    # group_required = ["user","observer","admin","super admins"]
    def get(self, request):
        posts = water_tank.objects.all()
        serializer = WaterTakeSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        node = WaterTakeSerializer(data=request.data)
        if node.is_valid():
            node.save()
            return Response(node.data, status=status.HTTP_201_CREATED)
        return Response(node.errors, status=status.HTTP_400_BAD_REQUEST)
    

class get_single_data(APIView):
    permission_classes = (IsAuthenticated, )
    # group_required = ["user","observer","admin","super admins"]
    def get(self, request ,id):
        posts = water_tank.objects.filter(id=id)
        serializer = WaterTakeSerializer(posts, many=True)
        return Response(serializer.data)
    

class get_single_data_with_rms(APIView):
    permission_classes = (IsAuthenticated, )
    # group_required = ["user","observer","admin","super admins"]
    def get(self, request ,rms):
        posts = water_tank.objects.filter(rms=rms)
        serializer = WaterTakeSerializer(posts, many=True)
        return Response(serializer.data)
    

class get_single_data_with_location(APIView):
    permission_classes = (IsAuthenticated, )
    # group_required = ["user","observer","admin","super admins"]
    def get(self, request ,location):
        posts = water_tank.objects.filter(location=location)
        serializer = WaterTakeSerializer(posts, many=True)
        return Response(serializer.data)
    

class get_single_data_with_district(APIView):
    permission_classes = (IsAuthenticated, )
    # group_required = ["user","observer","admin","super admins"]
    def get(self, request ,district):
        posts = water_tank.objects.filter(district=district)
        serializer = WaterTakeSerializer(posts, many=True)
        return Response(serializer.data)

class get_single_data_with_imei(APIView):
    permission_classes = (IsAuthenticated, )
    # group_required = ["user","observer","admin","super admins"]
    def get(self, request ,imei):
        posts = water_tank.objects.filter(district=imei)
        serializer = WaterTakeSerializer(posts, many=True)
        return Response(serializer.data)
    

class get_single_faulty_data(APIView):
    permission_classes = (IsAuthenticated, )
    # group_required = ["user","observer","admin","super admins"]
    def get(self, request):
        posts = water_tank.objects.filter(fault="True")
        serializer = WaterTakeSerializer(posts, many=True)
        return Response(serializer.data)

class get_time_data(APIView):
    permission_classes = (IsAuthenticated, )
    # group_required = ["user","observer","admin","super admins"]
    def get(self, request , rms):
        posts = water_tank_times.objects.filter(rms=rms)
        serializer = WaterTankTimeSerializer(posts, many=True)
        return Response(serializer.data)
    

class UserDetailAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)




# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })




class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    

from django.contrib.auth import logout
# @login_required(login_url='/')  # redirect when user is not logged in
def logout_view(request):
    logout(request)
    return redirect('/login')


def login_view(request):
    return render (request,"loginpage/login.html")

@login_required(login_url='/login')
def home(request):
    data =  water_tank.objects.all()
    if str(request.user.groups.all()[0]) == "superadmin" :
        return render (request,"home-SuperAdmin.html",{"data":data})
    else :
        return render (request,"home-Admin.html",{"data":data})

@login_required(login_url='/login')
def site_details(request):
    data =  water_tank.objects.all()
    return render (request,"siteDetails.html",{"data" : data})

@login_required(login_url='/login')
def alerts(request):
    return render (request,"alerts.html")

@login_required(login_url='/login')
def faults(request):
    return render (request,"faults.html")


@login_required(login_url='/login')
def index(request):
    return redirect ("/home")


from itertools import accumulate
from datetime import datetime , date
@login_required(login_url='/login')
def dashboard(request,rms):
    data =  water_tank.objects.filter(rms=rms).first()
    data2 =  water_tank_records.objects.filter(rms=rms).reverse().first()
    start_time = datetime.strptime((data2.start_time).strftime("%H:%M"), '%H:%M')
    stop_time = datetime.strptime((data2.stop_time).strftime("%H:%M"), '%H:%M')
    data3 =  water_tank_records_temp.objects.filter(rms=rms).reverse()
    run_time = start_time - stop_time
    return render (request,"dashboard/dashboard.html",{"data":data ,"run_time":run_time , "data2":data2 , "data3":data3})



def history_table(request,rms):
    data =  water_tank_records.objects.filter(rms=rms).reverse()#.first()
    data2 =  water_tank.objects.all()#.values_list("rms",flat=True)
    return render(request,'tableHistoricData.html',{"data":data,"data2":data2})


def history_table_search(request,rms,start_date,stop_date):
    data =  water_tank_records.objects.filter( rms=rms, date__range=(start_date, stop_date) )
    data2 =  water_tank.objects.all()#.values_list("rms",flat=True)
    return render(request,'tableHistoricData.html',{"data":data,"data2":data2})

def task_data(request):
    if cache.get('node'):
        return HttpResponse("incomplete")
    else:
        return HttpResponse("complete")


@login_required(login_url='/login')
def historicData(request):
    return render (request,"historicData.html")


@login_required(login_url='/login')
def historicData(request):
    return render (request,"historicData.html")

@csrf_exempt
def create_node (request) :
    if request.method == 'POST':
        dict_data = json.loads(request.body.decode('UTF-8'))
        topic = dict_data.get("topic")
        # print(dict_data)
        del dict_data['topic']

        if water_tank.objects.filter(rms = dict_data["rms"]).exists() :

            water_tank.objects.filter(rms = dict_data["rms"]).update(pump_status = dict_data["pump_status"] , signal_strength = dict_data["signal_strength"])

            water_tank_records.objects.create(rms = dict_data["rms"] , cumulative_lpd = dict_data["cumulative_lpd"] , current_lpm = dict_data["current_lpm"] , 
                                              voltage = dict_data["voltage"] , current = dict_data["current"] , power = dict_data["power"] , 
                                              wattage = dict_data["wattage"] , present_lpm = dict_data["present_lpm"] , start_time = dict_data["start_time"] , 
                                              stop_time = dict_data["stop_time"] , signal_strength = dict_data["signal_strength"] , run_time_today = dict_data["run_time_today"],
                                               time = dict_data["time"] )
            
            if water_tank_records_temp.objects.filter(rms = dict_data["rms"]).exists() :

                obj = water_tank_records_temp.objects.filter(rms = dict_data["rms"]).last()
            
                water_tank_records_temp.objects.create(rms = dict_data["rms"] , cumulative_lpd = obj.cumulative_lpd + float(dict_data["cumulative_lpd"]) , 
                                                       current_lpm = obj.current_lpm + float(dict_data["current_lpm"]) , voltage = obj.voltage + float(dict_data["voltage"]) , 
                                                       current = obj.current_lpm + float(dict_data["current"]) , power = obj.power + float(dict_data["power"]) , wattage = obj.wattage + float(dict_data["wattage"]) , 
                                                       present_lpm = obj.present_lpm + float(dict_data["present_lpm"]) , start_time = dict_data["start_time"] , 
                                                       stop_time = dict_data["stop_time"], signal_strength = dict_data["signal_strength"] ,  run_time_today = dict_data["run_time_today"],
                                                        time = dict_data["time"]  )
                cache.set("node", "changed",timeout=2)
                return HttpResponse ("done" , status=200)
        
            else :
                water_tank_records_temp.objects.create(rms = dict_data["rms"] , cumulative_lpd = float(dict_data["cumulative_lpd"]) , 
                                                       current_lpm = float(dict_data["current_lpm"]) , voltage = float(dict_data["voltage"]) , 
                                                       current =  float(dict_data["current"]) , power = float(dict_data["power"]) , wattage = float(dict_data["wattage"]) , 
                                                       present_lpm = float(dict_data["present_lpm"]) , start_time = dict_data["start_time"] , 
                                                       stop_time = dict_data["stop_time"],signal_strength = dict_data["signal_strength"] ,  run_time_today = dict_data["run_time_today"],
                                                        time = dict_data["time"]  )
                cache.set("node", "changed",timeout=2)
                return HttpResponse ("done" , status=200)
        else :
            return HttpResponse ("error2" ,status=404)
    return HttpResponse ("error3" ,status=404)
    




