from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('create-tweet/', views.create_tweet, name='create_tweet'),
    path('delete-tweet/<int:id>/', views.delete_tweet, name='delete_tweet'),
    path('logout/', views.logout_view, name='logout'),  # URL para logout
    path('', views.feed_view, name='feed'),  # Página inicial (feed)
    path('', include('django.contrib.auth.urls')),  # Inclui as rotas padrão de autenticação do Django
]
