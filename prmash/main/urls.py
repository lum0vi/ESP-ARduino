from django.urls import path
from . import views
from .views import get

    # остальные URL-маршруты вашего приложения...
urlpatterns = [
     path("home/", views.index, name="home"),
     path("get/", views.get, name="get"),
     path("blok/", views.index2, name="blok"),
     path("prch/", views.index3, name="prch"),
     path("dr/", views.index4, name="dr"),
     path("vp/", views.post1, name="vp"),
     path("prav/", views.post2, name="prav"),
     path("lev/", views.post3, name="lev"),
     path("naz/", views.post4, name="naz"),
     path("upr/", views.index5, name="upr"),
     path("sviat/", views.index6, name="sviat"),
     path("daria/", views.index7, name="daria"),
]