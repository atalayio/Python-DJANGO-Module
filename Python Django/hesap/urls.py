
from urllib import request
from django.contrib import admin
from django.urls import path
from pages.views import  (
    index,
    index2,
    alan,
    indirim,
    inc,
    aks,
    creatin,
    kdv,
    damgavergi,
    dibsinav,
    ehliyet,
    jana,
    kombiya,
    kurumlar,
    vucutk,
    mezuniyet,
    stopaj,
    noth,
    obph,
    sigara,
    su,
    uslus,
    vucuty,
    yas,
    yds,
    yuzde,
    zam,
    
   
)



urlpatterns = [
    path('index2/',index2,name="icerik"),
    path('',index, name="index"),
    path('admin/', admin.site.urls),
    path('alan/',alan, name="alan"),
    path('indirim/',indirim, name="indirim"),
    path('inc/',inc, name="inc"),
    path('aks/',aks, name="aks"),
    path('creatin/',creatin, name="creatin"),
    path('kdv/',kdv, name="kdv"),
    path('damgavergi/',damgavergi, name="damgavergi"),
    path('dibsinav/',dibsinav, name="dibsinav"),
    path('ehliyet/',ehliyet, name="ehliyet"),
    path('jana/',jana, name="jana"),
    path('kombiya/',kombiya, name="kombiya"),
    path('kurumlar/',kurumlar, name="kurumlar"),
     path('vucutk/',vucutk,name="vucutk"),
    path('mezuniyet/',mezuniyet,name="mezuniyet"),
    path('stopaj/',stopaj,name="stopaj"),
    path('noth/',noth,name="noth"),
    path('obph/',obph,name="obph"),
    path('sigara/',sigara,name="sigara"),
    path('su/',su,name="su"),
    path('uslus/',uslus,name="uslus"),
    path('vucuty/',vucuty,name="vucuty"),
    path('yas/',yas,name="yas"),
    path('yds/',yds,name="yds"),
    path('yuzde/',yuzde,name="yuzde"),
    path('zam/',zam,name="zam"),   
    
    


    

]
