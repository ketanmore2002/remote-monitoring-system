from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from node import views
from django.views.decorators.csrf import csrf_exempt
from knox import views as knox_views


urlpatterns = [
        path("api/data/",views.get_all_data.as_view(),name='get_all_data'),
        path("api/data/<str:id>/",views.get_single_data.as_view(),name='get_all_data'),
        path("api/rms/<str:rms>/",views.get_single_data_with_rms.as_view(),name='get_single_data_with_rms'),
        path("api/location/<str:location>/",views.get_single_data_with_location.as_view(),name='get_single_data_with_location'),
        path("api/district/<str:district>/",views.get_single_data_with_district.as_view(),name='get_single_data_with_district'),
        path("api/imei/<str:imei>/",views.get_single_data_with_imei.as_view(),name='get_single_data_with_imei'),

        path("api/time/<str:rms>/",views.get_time_data.as_view(),name='get_time_data'),
        
        path("api/fault/",views.get_single_faulty_data.as_view(),name='get_single_faulty_data'),
        path("api/login/",views.LoginAPI.as_view()),
        path('api/register/',views.RegisterAPI.as_view()),
        path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
        path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

        path('', views.index, name='index'),
        path('login', views.login_view, name='login'),
        path('home', views.home, name='home'),
        path('site_details', views.site_details, name='site_details'),
        path('alert', views.alerts, name='alerts'),
        path('fault', views.faults, name='faults'),
        path('logout', views.logout_view, name='logout_view'),
        
        path('dashboard/<str:rms>/', views.dashboard, name='dashboard'),
        path('historicData', views.historicData, name='historicData'),


  ]