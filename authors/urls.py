from django.urls import path
from authors import views

urlpatterns = [
    path('authors/', views.authors_list)
]