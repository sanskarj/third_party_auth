from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/<flag>/',views.message,name='message'),
    path('detail/<flag>/<idnumber>',views.detailview,name="detailview"),
    path('database/',views.entiredata,name="entiredata"),
    path('update/<idnumber>/',views.updatedata,name='updatedata')
   
]
