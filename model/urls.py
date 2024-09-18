from django.urls import path
from . import views




app_name = 'Model'
urlpatterns = [
    path('details/<int:pk>', views.ModelDetailsView.as_view(), name='ModelDetailsView'),
    path('dutch/', views.DutchModelListView.as_view(), name='DutchModelListView'),
    path('french/', views.FrenchModelListView.as_view(), name='FrenchModelListView'),
    path('mexican/', views.MexicanModelListView.as_view(), name='MexicanModelListView'),
    path('fishtail/', views.FishTailModelListView.as_view(), name='FishTailModelListView'),
    path('chignon/', views.ChignonModelListView.as_view(), name='ChignonModelListView'),
    path('journal/', views.JournalModelListView.as_view(), name='JournalModelListView'),
    path('spiral/', views.SpiralModelListView.as_view(), name='SpiralModelListView'),
    path('about/', views.AboutView.as_view(), name='AboutView'),
]




