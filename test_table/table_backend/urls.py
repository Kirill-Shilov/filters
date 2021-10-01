from django.urls import path
from . import views

urlpatterns = [
        path('api/table', views.TableList.as_view()),
        ]
