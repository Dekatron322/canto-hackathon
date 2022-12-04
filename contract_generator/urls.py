from django.urls import path
from . import views

app_name = "contract_generator"

urlpatterns = [
    path("", views.GeneratorView, name="contract_generator"),
    
]