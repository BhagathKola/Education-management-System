"""EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from EMS import settings
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('dept/',views.dept,name="dept"),
    path('placements/',views.placement,name="place"),
    path('contactno/', views.contact, name="contact"),
    path('Vexams/',views.examsView,name="Vexams"),
    #Admin URLs
    path('Ladmin/',views.admin,name="Ladmin"),
    path('Hadmin/',views.adminHome,name="Hadmin"),
    path('Weladmin/',views.welcomeAdmin,name="Weladmin"),
    path('Schdses/',views.schdSessions,name="Schdses"),
    path('Schexams/',views.schdExams,name="Schexams"),
    path('exams/',views.saveExams,name="exams"),

    path('SesSave/',views.seshses,name="SesSave"),
    path('viewfac/',views.viewFac,name="viewfac"),
    path('Fdelete/', views.facDelete, name='fdelete'),
    path('viewstud/',views.viewStud,name="viewstud"),
    path('Sdelete/', views.studDelete, name='Sdelete'),
    #Faculty Urls
    path('Flogin/',views.flogin,name="Flogin"),
    path('Freg/',views.fReg,name="Freg"),
    path('fsign/',views.fsign,name="fsign"),
    path('Fhome/',views.fHome,name="Fhome"),
    path('viewses/',views.sessions,name="Viewses"),
    path('assignment/',views.assignment,name="assignment"),
    path('saveAssign/',views.saveAssign,name="saveAssign"),
    path('SubAssign/',views.subAssignments,name="subassign"),


    #Student Urls
    path('Slogin/',views.slogin,name="Slogin"),
    path('Sreg/',views.sreg,name="Sreg"),
    path('signin/',views.signin,name="signin"),
    path('Shome/',views.shome,name="Shome"),
    path('Swelcome/',views.swelcome,name="Swelcome"),
    path('Stdses/',views.studSessions,name="Stdses"),
    path('SviewAss/',views.assignView,name="SviewAss"),
    path('Stsub/',views.studSubmit,name="studentsubmit"),
    path('saveDB/',views.saveDB,name="saveDB"),






    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico'))


    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)