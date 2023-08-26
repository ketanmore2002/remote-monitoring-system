from django.shortcuts import render ,redirect
from .models import *
from .Serializers import *
from rest_framework.permissions import IsAuthenticated
from braces.views import GroupRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import HttpResponse
from rest_framework import status
from django.contrib.auth.models import User ,Group
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

from datetime import datetime , date , time





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

    running = water_tank.objects.filter(pump_status="ON").count()
    not_running = water_tank.objects.filter(pump_status="OF").count()

    if str(request.user.groups.all()[0]) == "superadmin" :
        data =  water_tank.objects.all()
        return render (request,"home-SuperAdmin.html",{"data":data,"running":running,"not_running":not_running})
    else :
        data =  water_tank.objects.filter(created_by = request.user.id)
        return render (request,"home-Admin.html",{"data":data,"running":running,"not_running":not_running})
    

@login_required(login_url='/login')
def home_search(request,state,district,benificery_name):
    if str(request.user.groups.all()[0]) == "superadmin" :
        data =  water_tank.objects.filter(state=state,district=district,benificery_name=benificery_name)
        return render (request,"home-SuperAdmin.html",{"data":data})
    else :
        data =  water_tank.objects.filter(created_by = request.user.id,state=state,district=district,benificery_name=benificery_name)
        return render (request,"home-Admin.html",{"data":data})

@login_required(login_url='/login')
def site_details(request):
    data =  water_tank.objects.all()
    return render (request,"siteDetails.html",{"data" : data})

@login_required(login_url='/login')
def site_details_search(request,rms):
    data =  water_tank.objects.filter(rms=rms).first()
    data2 =  water_tank.objects.all()
    return render (request,"siteDetails_search.html",{"data" : data, "data2" : data2})

from django.shortcuts import render, redirect
from .models import water_tank
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def register_pump(request):
    if request.method == 'POST':
        # Get form data from request.POST
        contractor_name = request.POST.get('ContractorName')
        beneficiary_name = request.POST.get('BeneficiaryName')
        site_address = request.POST.get('SiteAddress')
        district = request.POST.get('District')
        state = request.POST.get('State')
        date_of_installation = request.POST.get('DateofInstallation')
        capacity = request.POST.get('Capacity')
        make = request.POST.get('Make')
        pump_model_no = request.POST.get('PumpModelNo')
        controller_model_no = request.POST.get('ControllerModelNo')
        pump_serial_no = request.POST.get('PumpSerialNo')
        controller_serial_no = request.POST.get('ControllerSerialNo')
        rms_id = request.POST.get('RMSID')
        modem_id = request.POST.get('ModemID')
        sim_id = request.POST.get('SIMID')
        iccid = request.POST.get('ICCID')
        head = request.POST.get('Head')
        
        # Create and save a new water_tank instance
        water_tank_obj = water_tank(
            contractor_name=contractor_name,
            benificery_name=beneficiary_name,
            site_address=site_address,
            district=district,
            state=state,
            installation_date=date_of_installation,
            capacity=capacity,
            make=make,
            pump_model_number=pump_model_no,
            controller_model_number=controller_model_no,
            pump_serial_numbers=pump_serial_no,
            controller_serial_numbers=controller_serial_no,
            rms=rms_id,
            modem_id=modem_id,
            sim_id=sim_id,
            iccid=iccid,
            created_by = request.user.id,
            head = head
        )
        water_tank_obj.save()
        
        # Redirect to a success page or do any other necessary actions
        return redirect('/')  # Change 'success_page' to your desired URL

    return render(request, "registration.html")


@login_required(login_url='/login')
def alerts(request):
    return render (request,"alerts.html")

@login_required(login_url='/login')
def faults(request):
    return render (request,"faults.html")


@login_required(login_url='/login')
def index(request):
    return redirect ("/home")


@login_required(login_url='/login')
def dashboard(request,rms):
    data =  water_tank.objects.filter(rms=rms).first()
    data2 =  water_tank_records.objects.filter(rms=rms).reverse().last()
    data3 =  water_tank_records_temp.objects.filter(rms=rms).reverse()
    try :
        start_time = datetime.strptime((data2.start_time).strftime("%H:%M"), '%H:%M')
        stop_time = datetime.strptime((data2.stop_time).strftime("%H:%M"), '%H:%M')
        run_time = stop_time - start_time 
        return render (request,"dashboard/dashboard.html",{"data":data ,"run_time":run_time , "data2":data2 , "data3":data3})
    except:
        return render (request,"dashboard/dashboard.html",{"data":data , "data2":data2 , "data3":data3})



def history_table(request,rms):
    data =  water_tank_records.objects.filter(rms=rms).reverse()#.first()
    data2 =  water_tank.objects.all()#.values_list("rms",flat=True)
    return render(request,'tableHistoricData.html',{"data":data,"data2":data2})


def history_table_search(request,rms,start_date,stop_date):
    data =  water_tank_records.objects.filter( rms=rms, date__range=(start_date, stop_date) )
    data2 =  water_tank.objects.all()#.values_list("rms",flat=True)
    return render(request,'tableHistoricData.html',{"data":data,"data2":data2})


# voltage_std = (list(voltage_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('voltage', flat=True)) )


def graph_search(request,rms,start_date,stop_date):
    
    run_time =  list(water_tank_records.objects.filter( rms=rms, date__range=(start_date, stop_date)).values_list("run_time_today",flat=True))
    run_time = [time_obj.strftime("%H:%M") for time_obj in run_time]
    date =  list(water_tank_records.objects.filter( rms=rms, date__range=(start_date, stop_date)).values_list("date",flat=True))
    date = [date_obj.strftime("%Y-%m-%d") for date_obj in date]

    return render(request,'graph/graphHistoricData.html',{"run_time":run_time,"date":date})

from django.contrib.auth.models import User
def costumer_management(request):

    if str(request.user.groups.all()[0]) == "superadmin" :
        data = User.objects.all()
        return render(request,'costumerManag.html',{"data":data})
    else:
        return redirect("/")

def task_data(request):
    if cache.get('node'):
        return HttpResponse("incomplete")
    else:
        return HttpResponse("complete")


@login_required(login_url='/login')
def historicData(request):
    return render (request,"historicData.html")


@login_required(login_url='/login')
def user_data_create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        user_role = request.POST.get('user_role')
        User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password)
        user = User.objects.get(username=username)  # Replace 'username_here' with the actual username
        group, created = Group.objects.get_or_create(name=user_role)
        user.groups.set([group])
        return redirect("/costumer_management")
    
    return render (request,"user.html")


@login_required(login_url='/login')
def user_data_update(request,id):
    user = User.objects.get(id=id)  # Replace 'username_here' with the actual username
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        user_role = request.POST.get('user_role')
        
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save()

        group, created = Group.objects.get_or_create(name=user_role)
        user.groups.clear() 
        user.groups.add(group) 
        return redirect("/costumer_management")
    
    return render (request,"user_update.html",{"data":user})

@login_required(login_url='/login')
def user_data_delete(request,id):
    User.objects.get(id=id).delete()  # Replace 'username_here' with the actual username
    return redirect("/costumer_management")

@csrf_exempt
def create_node (request) :
    if request.method == 'POST':
        dict_data = json.loads(request.body.decode('UTF-8'))
        topic = dict_data.get("topic")
        # print(dict_data)
        del dict_data['topic']

        if water_tank.objects.filter(rms = dict_data["rms"]).exists() :

            # start_time = datetime.strptime(dict_data["start_time"], "%H:%M:%S").time()
            # stop_time = datetime.strptime(dict_data["stop_time"], "%H:%M:%S").time()

            start_time = datetime.strptime(dict_data["start_time"],"%H:%M").time()
            stop_time = datetime.strptime(dict_data["stop_time"],"%H:%M").time()

            # run_time_today = start_time - stop_time

            run_time_today = datetime.combine(date.min, stop_time) - datetime.combine(date.min, start_time)

            print(run_time_today)

            if water_tank_records_temp.objects.filter(rms = dict_data["rms"]).exists() :

                obj = water_tank_records_temp.objects.filter(rms = dict_data["rms"]).last()

                cumulative_lpd = obj.cumulative_lpd + float(dict_data["present_lpm"])
            
                water_tank_records_temp.objects.create(rms = dict_data["rms"] , cumulative_lpd = cumulative_lpd ,voltage = float(dict_data["voltage"]) , 
                                                       current = float(dict_data["current"]) , power = float(dict_data["power"]) , wattage = float(dict_data["wattage"]) , 
                                                       present_lpm = float(dict_data["present_lpm"]) , start_time = dict_data["start_time"] , 
                                                       stop_time = dict_data["stop_time"], signal_strength = dict_data["signal_strength"] ,
                                                       run_time_today = str(run_time_today))
        
            else :

                cumulative_lpd = float(dict_data["present_lpm"])

                water_tank_records_temp.objects.create(rms = dict_data["rms"] , cumulative_lpd = cumulative_lpd , 
                                                       voltage = float(dict_data["voltage"]) , 
                                                       current =  float(dict_data["current"]) , power = float(dict_data["power"]) , wattage = float(dict_data["wattage"]) , 
                                                       present_lpm = float(dict_data["present_lpm"]) , start_time = dict_data["start_time"] , 
                                                       stop_time = dict_data["stop_time"],signal_strength = dict_data["signal_strength"] ,
                                                       run_time_today = str(run_time_today),)
                

            water_tank_records.objects.create(rms = dict_data["rms"] , cumulative_lpd = cumulative_lpd ,voltage = dict_data["voltage"] , 
                                              current = dict_data["current"] , power = dict_data["power"] , 
                                              wattage = dict_data["wattage"] , present_lpm = dict_data["present_lpm"] , start_time = dict_data["start_time"] , 
                                              stop_time = dict_data["stop_time"] , signal_strength = dict_data["signal_strength"] ,
                                              run_time_today = str(run_time_today),)
            
            water_tank.objects.filter(rms = dict_data["rms"]).update(pump_status = dict_data["pump_status"] , signal_strength = dict_data["signal_strength"])
            
            cache.set("node", "changed",timeout=2)
            return HttpResponse ("done" , status=200)
        
        else :
            return HttpResponse ("error2" ,status=404)
    return HttpResponse ("error3" ,status=404)
    




