from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.each_pu, name='each_pu'),
    path('lga/', views.lga, name='lga'),
    path('lga/<int:id>', views.each_lga, name='each_lga'),
]
