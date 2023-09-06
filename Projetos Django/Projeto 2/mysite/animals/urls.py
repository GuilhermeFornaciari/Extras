from django.urls import path

from . import views
app_name = "animals"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:animal_id>/', views.animaldetail,name='detail'),
    path('habitats/<int:habitat_id>/', views.habitatview,name='habitat'),
    path('<int:animal_id>/vote/', views.voteanimal,name='vote'),
]