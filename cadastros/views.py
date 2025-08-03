from django.db import connection
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Cliente, Produto, Venda

# Criar Cadastros de Produto e Cliente

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'email', 'cidade', 'estado', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-cliente')


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'cadastros/produto.html'
    success_url = reverse_lazy('lista-produto')
    fields = ['descricao', 'marca_produto', 'detalher_produto', 'data_chegada', 'quantidade', 'preco_unitario', 'valor']

    def form_valid(self, form):
        quantidade = form.cleaned_data['quantidade']
        preco_unitario = form.cleaned_data['preco_unitario']
        form.instance.valor = quantidade * preco_unitario
        return super().form_valid(form)


# Editar Cliente e Produto

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'cidade', 'estado', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-cliente')


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['descricao', 'marca_produto', 'detalher_produto', 'data_chegada']
    template_name = 'cadastros/produto.html'
    success_url = reverse_lazy('lista-produto')


# Deletar Cliente e Produto

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('lista-cliente')


class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('lista-produto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir produto'
        return context

class VendaCreate(CreateView):
    model = Venda
    template_name = 'cadastros/form_venda.html'
    fields = ['cliente', 'produto', 'quantidade', 'preco_unitario']
    success_url = reverse_lazy('lista-vendas')

    def form_valid(self, form):
        form.instance.subtotal = form.cleaned_data['quantidade'] * form.cleaned_data['preco_unitario']
        return super().form_valid(form)


# Listagens

class ProdutoList(ListView):
    model = Produto
    template_name = 'cadastros/listas/lista_produto.html'


class ClienteList(ListView):
    model = Cliente
    template_name = 'cadastros/listas/lista_cliente.html'


class ListVenda(ListView):
    model = Venda
    template_name = 'cadastros/listar-venda.html'
    success_url = reverse_lazy('lista-vendas')

    def get_queryset(self):
        queryset = super().get_queryset()
        for venda in queryset:
            venda.subtotal = venda.quantidade * venda.preco_unitario
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendas = context['object_list']
        context['total'] = sum(v.subtotal for v in vendas)
        return context


# Pesquisas

class PesquisarProduto(ListView):
    model = Produto
    template_name = 'cadastros/listas/lista_produto.html'

    def get_queryset(self):
        queryset = Produto.objects.all().order_by('descricao')
        descricao = self.request.GET.get('descricao')
        if descricao:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM cadastros_produto WHERE descricao LIKE %s", ['%' + descricao + '%'])
                resultados = cursor.fetchall()
            produto_ids = [r[0] for r in resultados]
            queryset = Produto.objects.filter(pk__in=produto_ids)
        return queryset


class Pesquisar(ListView):
    model = Cliente
    template_name = 'cadastros/listas/lista_cliente.html'

    def get_queryset(self):
        queryset = Cliente.objects.all().order_by('nome')
        nome = self.request.GET.get('nome')
        if nome:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM cadastros_cliente WHERE nome LIKE %s", ['%' + nome + '%'])
                resultados = cursor.fetchall()
            cliente_ids = [r[0] for r in resultados]
            queryset = Cliente.objects.filter(pk__in=cliente_ids)
        return queryset
