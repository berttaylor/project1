from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>/', views.entry_detail, name='entry_detail'),
    path('wiki/<str:title>/edit_page.html', views.edit_page, name="edit_page"),
    path('search_results/', views.search_results, name='search_results'),
    path('wiki/404', views.page_not_found, name='page_not_found'),
    path('save_new_page', views.save_new_page, name='save_new_page'),
    path('new_page.html', views.new_page, name="new_page"),
    path('random', views.random_page, name="random_page"),
]
    
    
