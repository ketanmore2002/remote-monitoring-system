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
    return render (request,"home.html",{"data":data})

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


@login_required(login_url='/login')
def dashboard(request,rms):
    data =  water_tank.objects.filter(rms=rms).first()
    # time_data =  water_tank_times.objects.filter(rms=rms).first()
    return render (request,"dashboard/dashboard.html",{"data":data })


@login_required(login_url='/login')
def historicData(request):
    return render (request,"historicData.html")