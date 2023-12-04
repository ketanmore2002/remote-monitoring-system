from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from node import views
from django.views.decorators.csrf import csrf_exempt
from knox import views as knox_views


urlpatterns = [
      #   path("api/data/",views.get_all_data.as_view(),name='get_all_data'),
      #   path("api/data/<str:id>/",views.get_single_data.as_view(),name='get_all_data'),
      #   path("api/rms/<str:rms>/",views.get_single_data_with_rms.as_view(),name='get_single_data_with_rms'),
      #   path("api/location/<str:location>/",views.get_single_data_with_location.as_view(),name='get_single_data_with_location'),
      #   path("api/district/<str:district>/",views.get_single_data_with_district.as_view(),name='get_single_data_with_district'),
      #   path("api/imei/<str:imei>/",views.get_single_data_with_imei.as_view(),name='get_single_data_with_imei'),

      #   path("api/time/<str:rms>/",views.get_time_data.as_view(),name='get_time_data'),
        
      #   path("api/fault/",views.get_single_faulty_data.as_view(),name='get_single_faulty_data'),
        path("api/login/",views.LoginAPI.as_view()),
      #   path('api/register/',views.RegisterAPI.as_view()),
      #   path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
      #   path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

        path('', views.index, name='index'),
        path('login', views.login_view, name='login'),
        path('home', views.home, name='home'),
        path('home/search/<str:state>/<str:district>/<str:benificery_name>/', views.home_search, name='home_search'),
        path('site_details', views.site_details, name='site_details'),
        path('site_details/search/<str:rms>/', views.site_details_search, name='site_details'),
        path('alert', views.alerts, name='alerts'),
        path('fault', views.faults, name='faults'),
        path('logout/', views.logout_view, name='logout_view'),
        
        path('dashboard/<str:rms>/', views.dashboard, name='dashboard'),
        path('historicData', views.historicData, name='historicData'),
        path('create_node/', views.create_node, name='create_node'),

        path("task_data/",views.task_data,name='task_data'),
        path("history_table/<str:rms>/",views.history_table,name='history_table'),
        path("history_table/search/<str:rms>/<str:start_date>/<str:stop_date>/",views.history_table_search,name='history_table'),
        path("register_pump/",views.register_pump,name='register_pump'),
        path("costumer_management/",views.costumer_management,name='costumer_management'),
        path("user_data_create/",views.user_data_create,name='user_data_create'),
        path("user_data_update/<int:id>/",views.user_data_update,name='user_data_update'),
        path("user_data_delete/<int:id>/",views.user_data_delete,name='user_data_delete'),
        path("graph/search/<str:rms>/<str:start_date>/<str:stop_date>/",views.graph_search,name='graph_search'),
        path("edit/<str:rms>/",views.edit_pump,name='edit_pump'),
        path("delete/<str:rms>/",views.delete_pump,name='delete_pump'),
        path("version/",views.version,name='version'),
  ]