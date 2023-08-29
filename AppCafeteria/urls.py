from django.urls import path
from .views import *


urlpatterns = [
        path("cafeterias/", cafeterias, name="cafeterias"),
        path("baristas/", baristas, name= "baristas"),
        path("comunidad/", comunidad, name="comunidad"),
        path("busquedacafeteria/", busquedaCafeteria, name= "busquedacafeteria"),
        path("buscar/", buscar, name="buscar"), 

]