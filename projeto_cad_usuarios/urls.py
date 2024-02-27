


from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota de view responsivel, nome de referencia 
    # cadastros.com
    path('',views.home,name = 'home.html'),

    path('usuarios/', views.usuarios,name='listagem_usuarios')
   
   
]
