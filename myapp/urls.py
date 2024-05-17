from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='home'),
    path('loginpage' , views.Login.as_view(), name='login'),
    path('adduser'  , views.AddUserMaster.as_view() , name='adduser'),
    path('adduserprofile',views.AddUserProfile.as_view(),name='adduserprofile'),
    path('logout' , views.logouts , name='logouts'),
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
    
    #url for Buyers
    path('srch',views.Search.as_view(),name='srch'),
    path('getpro',views.getProduct,name='getpro'),
    path('showcart',views.CartMgmt.as_view(),name="showcart"),
    path('delcart/<id>',views.deleteProduct,name='delcart'),
    path('showorder',views.showOrder,name="showorder"),

    #urls for Compalint
    path('addcomp',views.AddComplaint.as_view(),name='addcomp'),
    path('showcomps',views.showComplaints,name='showcomps'),
    path('response/<id>',views.Response.as_view(),name='response'),
]