from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index-post'),
    path('post/', views.lista_posts, name="lista-post"),
    path('post/<int:post>',views.post, name='pagina-post'),
]
