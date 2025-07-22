from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ClienteCreate, ListVenda, Pesquisar, PesquisarProduto, ProdutoCreate ,ClienteUpdate, ProdutoUpdate, ClienteDelete,ClienteList,ProdutoList, Venda
from .views import ProdutoDelete




urlpatterns = [
   # CRIAR CADASTROS
   path('cadastros/',ClienteCreate.as_view(), name='cadastros'),
   path('produto/',ProdutoCreate.as_view(),name='produto'),
    ## EDITAR   
   path('editar/cliente/<int:pk>/' , ClienteUpdate.as_view(), name='editar-cliente'),
   path('editar/produto/<int:pk>/' ,ProdutoUpdate.as_view(), name='editar-produto'),
   ## APAGAR
   path('excluir/cliente/<int:pk>/' , ClienteDelete.as_view(), name='excluir-cliente'),
   path('excluir/produto/<int:pk>/' , ProdutoDelete.as_view(), name='excluir-produto'),
   # lista banco de dados
   path('lista/cliente/' , ClienteList.as_view(), name='lista-cliente'),
   path('lista/produto/' ,ProdutoList.as_view(), name='lista-produto'),
   # pesquisa produro
   path('Pesquisar/', Pesquisar.as_view(), name='Pesquisar'),
   path('Produto/', PesquisarProduto.as_view(), name='pesquisar-produto'),
   ### tebela de venda 
    
    path('vendas/', ListVenda.as_view(), name='lista-vendas'),
]

