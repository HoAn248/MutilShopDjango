from django.urls import path 
from . import views 
urlpatterns = [ 
path('cart/', views.cart),
path('cart/<int:id>', views.deleteProduct),
path('signin/', views.signin),
path('signup/', views.signup),
]
