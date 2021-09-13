from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('post/<int:post>',views.post, name='pagina-post'),
]
