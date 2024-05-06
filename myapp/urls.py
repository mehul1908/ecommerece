from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='home'),
    path('loginpage' , views.Login.as_view(), name='login'),
    path('adduser'  , views.AddUserMaster.as_view() , name='adduser'),
    path('adduserprofile',views.AddUserProfile.as_view(),name='adduserprofile'),
    path('logout' , views.logouts , name='logout'),
    path('showuser',views.showuser , name='showuser'),
    path('edituser/<str:id>',views.edituser.as_view() , name='edituser'),
    path('deluser/<str:id>',views.deluser,name='deluser'),
    #product category
    path('addprocat',views.AddProdCat.as_view(),name='addprocat'),
    path('showprocat',views.showProCat,name='showprocat'),
    path('editprocat/<str:id>',views.editprocat.as_view() , name='editprocat'),
    path('delprocat/<str:id>',views.delprocat,name='delprocat'),

    #product

    path('addpro',views.AddProd.as_view(),name='addpro'),
    path('showpro',views.showPro,name='showpro'),
    path('editpro/<str:id>',views.editpro.as_view() , name='editpro'),
    path('delpro/<str:id>',views.delpro,name='delpro'),
    
]