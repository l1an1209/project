from django.views.generic import TemplateView


class indexView(TemplateView):
    template_name = 'index.html'

class modeloView(TemplateView):
    template_name = 'modelo.html'

    

class sobreView(TemplateView):
    template_name = 'sobre.html'

class movimentoView(TemplateView):
    template_name = 'movimento.html'

class estoqueView(TemplateView):
    template_name = 'estoque.html'
