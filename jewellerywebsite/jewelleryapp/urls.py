from . import views
from django.urls import path
app_name='jewelleryapp'

urlpatterns = [
    path('',views.index,name='index'),
]