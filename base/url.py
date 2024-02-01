from django.urls import path
from .views import drink , drink_detail

urlpatterns = [
    path('drinks/', drink , name="drinks"),
    path('drinks/<int:id>',drink_detail,name="drinkdetail"),
]
