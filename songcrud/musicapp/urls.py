from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('song', views.Song_list),
    path('song/<int:id>', views.Song_detail),
    path('artiste', views.Artiste_list),
    path('artiste/<int:id>', views.Artiste_detail)
    
]