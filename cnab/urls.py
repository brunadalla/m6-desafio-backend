from django.urls import path
from .views import cnab_view
  
urlpatterns = [
    path('', cnab_view.as_view() ),
]