from django.urls import path, include
from . import views 

urlpatterns = [
    path("", views.kanban_home, name="kanban_home"),
    path("cfd_chart/", views.cfd_chart_view, name="cfd_chart"),
]