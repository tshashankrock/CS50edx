from django.conf.urls import url
from first_app import views
from django.urls import path
#template tagging

app_name = 'first_app'

urlpatterns = [
    url(r'^cart/',views.cart,name='cart'),
    #url(r'^$', views.form_name_view, name='form_name'),  #is line ka matlab hai jab 127.0.0.1:8000 ho tab index.html call ko index function sa view.py ma
    #url(r'^signup/', views.signup, name='signup'),
    #url(r'^menu/',views.menu,name = 'menu'),
    #url(r'^welcome/',views.welcome,name = 'welcome'),
    #url(r'^logout/', views.logout, name='logout'),
#    url('r^admin/',views.admin,name='admin')
]
#/home/shashank/gitprac/CS50edx/lecture7/project3/first_project/first_app/urls.py
