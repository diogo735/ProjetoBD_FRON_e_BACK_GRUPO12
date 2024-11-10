from django.contrib import admin
from django.urls import path
from app_escola import views  # Importa as views do app
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('login/', views.login_view, name='login'),
    path('pagina_principal/', views.pagina_principal, name='pagina_principal'),
    path('loading/', views.loading_page, name='loading_page'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    #opções da nav bar
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calendario/', views.calendario, name='calendario'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('aulas/', views.aulas, name='aulas'),
    path('pagamentos/', views.pagamentos, name='pagamentos'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('gestao_escola/', views.gestao_escola, name='gestao_escola'),
    
]
