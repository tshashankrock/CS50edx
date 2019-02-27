"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from first_app import views
from django.conf.urls import url,include

""" url(r'^cart/',include('first_app.urls')),
    url(r'^logout/',include('first_app.urls')),
    url(r'^$',views.form_name_view,name='form_name'),
    url(r'^signup/',include('first_app.urls')),
    url(r'^menu/',include('first_app.urls')),
    url(r'^welcome/',include('first_app.urls')),
"""

urlpatterns = [
    url(r'first_app/',include('first_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^$', views.form_name_view, name='form_name'),  #is line ka matlab hai jab 127.0.0.1:8000 ho tab index.html call ko index function sa view.py ma
    url(r'^signup/', views.signup, name='signup'),
    url(r'^menu/',views.menu,name = 'menu'),
    url(r'^welcome/',views.welcome,name = 'welcome'),
    url(r'^logout/', views.logout, name='logout'),
    #path('signup/',include('first_app.urls')),  #is line ka matlab hai jab 127.0.0.1:8000/sigup/ ho tab signup function call ko view.py sa iski mapping urls.py ma hui hai jo ki first_app hai.
    #path('formpage/',views.form_name_view,name = 'form_name'),
]
#/home/shashank/gitprac/CS50edx/lecture7/project3/first_project/first_project/urls.py
