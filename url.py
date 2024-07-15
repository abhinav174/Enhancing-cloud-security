from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users import views
from users.views import index,userlogin,adminlogin,cloudlogin,userregister,storeregistration,logout,userlogincheck,usercreateapp,appcreaterequest,useruploadfile,snippet_detail
from admins.views import adminlogincheck,adminactivateusers,activatewaitedusers
from clouds.views import activateuserapp,cloudlogincheck,clouduserappactivations
from .views import resturl,downloadfile,deletefile,uploadfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path(r'accounts', views.AccountAPIView.as_view(), name='account-list'),
    path(r'contacts', views.ContactAPIView.as_view(), name='contact-list'),
    path(r'activities', views.ActivityAPIView.as_view(), name='activity-list'),
    path(r'activitystatuses', views.ActivityStatusAPIView.as_view(), name='activity-status-list'),
    path(r'contactsources', views.ContactSourceAPIView.as_view(), name='contact-source-list'),
    path(r'contactstatuses', views.ContactStatusAPIView.as_view(), name='contact-status-list'),
    path(r'logout',logout,name='logout'),

    path(r'adminlogincheck',adminlogincheck,name='adminlogincheck'),
    path(r'adminactivateusers',adminactivateusers,name='adminactivateusers'),
    path(r'activatewaitedusers/<id>/$',activatewaitedusers,name='activatewaitedusers'),

    path(r'userlogin',userlogin,name='userlogin'),
    path(r'adminlogin', adminlogin, name='adminlogin'),
    path(r'cloudlogin', cloudlogin, name='cloudlogin'),
    path(r'userregister', userregister, name='userregister'),
    path(r'storeregistration',storeregistration,name='storeregistration'),
    path(r'userlogincheck', userlogincheck, name='userlogincheck'),
    path(r'usercreateapp',usercreateapp,name='usercreateapp'),
    path(r'appcreaterequest',appcreaterequest,name='appcreaterequest'),
    path(r'useruploadfile/<appname>/$',useruploadfile,name='useruploadfile'),
    path(r'^snippet_detail/$',snippet_detail,name='snippet_detail'),

    path(r'resturl/<id>',resturl,name='resturl'),
    path(r'downloadfile/<id>',downloadfile,name='downloadfile'),
    path(r'deletefile/<id>',deletefile,name='deletefile'),
    path(r'uploadfile',uploadfile,name='uploadfile'),


    path(r'activateuserapp',activateuserapp,name='activateuserapp'),
    path(r'cloudlogincheck',cloudlogincheck,name='cloudlogincheck'),
    path(r'clouduserappactivations/<appname>/$',clouduserappactivations, name='clouduserappactivations'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

