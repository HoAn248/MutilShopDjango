from django.urls import path 
from . import views 
urlpatterns = [ 
path('', views.shop),
path('<int:id>', views.detail)
]
