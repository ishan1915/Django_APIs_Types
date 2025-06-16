from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

#for viewsets api urls
router=DefaultRouter()
router.register(r'items',ItemViewSet) 
router.register(r'itemsa', ItemReadOnlyViewSet ,basename='item-readonly')



urlpatterns = [
    path('hello/', HelloWorld.as_view()),
    path('s/', ItemStatsAPIView.as_view()),

    path('h1/',ItemCreateView.as_view()),
    path('h3/', ItemListView.as_view()),

    path('h2/<int:pk>/', ItemRetrieveView.as_view()),
    path('h4/<int:pk>/',ItemUpdateView.as_view()),
    path('h5/',ItemListCreateView.as_view()),
    path('h6/<int:pk>/',ItemDetailView.as_view()),
    path('h7/', ItemCustomView.as_view(), name='item-custom'),
    path('h8/', simple_viewa, name='item-custom'),



]
urlpatterns += router.urls
