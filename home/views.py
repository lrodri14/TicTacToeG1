from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class Cargando(View):

    template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name)


class Home(View):

    template_name = 'home/home.html'

    def get(self, request):
        return render(request, self.template_name)



