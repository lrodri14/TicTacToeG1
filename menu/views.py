from django.shortcuts import render
from django.views.generic import View
from autenticacion.models import Record

# Create your views here.


class Menu(View):

     template_name = 'menu/menu.html'

     def get(self, request):
         username = request.user.username
         record = Record.objects.get(jugador=request.user)
         context = {'username': username, 'record': record}
         return render(request, self.template_name, context=context)