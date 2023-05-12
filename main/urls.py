from django.urls import path

from .views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('user_work/<pk>/', userWork, name='user_work'),
    path('work_objects/', WorkObjects.as_view(), name='work_objects'),
    path('create_work_object/', createWorkObject, name='create_work_object'),
    path('work_object/<pk>/', workObjectView, name='work_object'),
    path('user_raport/<user_pk>/', getUserRaport, name='user_raport'),
    path('workobject_raport/<user_pk>/<object_pk>/', getObjectRaport, name='workobject_raport'),
    ]