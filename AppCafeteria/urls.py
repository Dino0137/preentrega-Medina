from django.urls import path
from .views import *


urlpatterns = [
        path("cafeterias/", cafeterias, name="cafeterias"),
        path("crear_cafeteria/", crear_cafeteria),
        path("listar_cafeterias/", listar_cafeterias),
        path("baristas/", baristas, name= "baristas"),
        path("comunidad/", comunidad, name="comunidad"),

]