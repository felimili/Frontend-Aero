"""AeroFront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path 
from app.crud.views import  inicio, login, usuarios, altauser, alta_avion, editar, eliminar, aviones, eliminar_avion, editar_avion,vuelos,altavuelo, eliminar_vuelo, editar_vuelo, upload, download
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name = 'login'),
    path('altauser/', altauser, name = 'altauser'),
    path ('', inicio, name= 'inicio'),
    path('vuelos/', vuelos, name='vuelos'),
    path('altavuelo/', altavuelo, name='altavuelo'),
    path('editarvuelo/<int:id>', editar_vuelo, name = 'editarvuelo' ),
    path('usuarios/', usuarios, name = 'usuarios' ),
    path('aviones/', aviones, name = 'aviones' ),
    path('altaavion/', alta_avion, name = 'altaavion' ),
    path('editar/<int:id>', editar, name = 'editar' ),
    path('eliminar/<int:id>', eliminar, name = 'eliminar' ),
    path('editaravion/<int:id>', editar_avion, name = 'editaravion' ),
    path('eliminaravion/<int:id>', eliminar_avion, name = 'eliminaravion' ),
    path('eliminarvuelo/<int:id>', eliminar_vuelo, name = 'eliminarvuelo' ),
    path('upload/<int:id>', upload, name = 'upload'),
    path('download/<int:id>', download, name = 'download'),
    
    
]
