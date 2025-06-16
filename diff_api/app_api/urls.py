from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', HelloWorld.as_view()),
    path('h1/',ItemCreateView.as_view()),
    path('h3/', ItemListView.as_view()),

    path('h2/<int:pk>/', ItemRetrieveView.as_view()),
    path('h4/<int:pk>/',ItemUpdateView.as_view()),
    path('h5/',ItemListCreateView.as_view()),
    path('h6/<int:pk>/',ItemDetailView.as_view()),

]