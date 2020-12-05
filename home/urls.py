from django.urls import path , include
from . import views

app_name = 'home'


urlpatterns = [
    path('', views.home),
    path('breakfast/', views.breakfast_meals , name = 'primary'),
    path('breakfast/<int:id>', views.breakfast_details , name = 'secondary'),
    path('lunch/', views.lunch_meals , name = 'lunch_primary'),
    path('lunch/<int:id>', views.lunch_details , name = 'lunch_secondary'),
    path('dinner/', views.dinner_meals , name = 'dinner_primary'),
    path('dinner/<int:id>', views.dinner_details , name = 'dinner_secondary'),
]
