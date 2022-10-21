from django.urls import path
from formcrudoperationapp import views

urlpatterns=[
    path("",views.student),
    path('table/',views.Table,name='table'),
    path('delete/<int:id>/',views.Delete,name='delete'),
    path('update/<int:id>/',views.Update,name="update")

]