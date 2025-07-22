from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import indexView , modeloView, sobreView, movimentoView, estoqueView


urlpatterns = [
    path('',indexView.as_view(),name='inicio'),
    path('modelo/', modeloView.as_view(), name='modelo' ),
    path('sobre/', sobreView.as_view(), name='sobre'),
    path('movimento/', movimentoView.as_view(), name='movimento'),
    path('estoque/',estoqueView.as_view(),name='estoque'),
   
]

