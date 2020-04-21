from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:id>", views.edititem, name = "edit"),
    path("create",views.create, name = "createitem"),
    path("delete/<int:id>",views.delete, name= "delete"),
    path("<int:id>",views.itemdetails, name = 'itemdetails'),
    path("register",views.register, name= 'register'),
    path('login', views.loginpage, name='loginpage'),
    path('logout',views.logout_page, name= 'logout'),
]
