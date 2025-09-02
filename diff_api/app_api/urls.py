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
    path('create-form/', item_create_form, name='item-create-form'),


    path('h3/', ItemListView.as_view()),

    path('h2/<int:pk>/', ItemRetrieveView.as_view()),
    path('h4/<int:pk>/',ItemUpdateView.as_view()),
    path('h5/',ItemListCreateView.as_view()),
    path('h6/<int:pk>/',ItemDetailView.as_view()),
    path('h7/', ItemCustomView.as_view(), name='item-custom'),
    path('h8/', simple_viewa, name='item-custom'),

     path('', login_page, name='login_page'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),


    path('add/',add_view,name='add'),
    path('sub/',sub_view,name='sub'),
    path('mul/',mul_view,name='mul'),
    path('div/',div_view,name='div'),
    path('fact/',fact_view,name='fact'),
    path('pow/',pow_view,name='pow'),



]
urlpatterns += router.urls
