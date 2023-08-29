from django.urls import path
from .views import *


urlpatterns = [
        path("cafeterias/", cafeterias, name="cafeterias"),
        path("baristas/", baristas, name= "baristas"),
        path("comunidad/", comunidad, name="comunidad"),
        path("busquedaCafeteria/", busquedaCafeteria, name= "busquedaCafeteria"),
        path("buscar/", buscar, name="buscar"), 

]