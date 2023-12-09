from django.shortcuts import render
from django.views.generic import View
from autenticacion.models import Record

# Create your views here.


class Estadisticas(View):

    template_name = 'stats/estadisticas.html'

    def get(self, request):
        usuario = request.user
        record = usuario.record.first()
        records = Record.objects.all().order_by('-puntos')
        context = {'usuario': record, 'records': records, 'username': usuario.username}
        return render(request, self.template_name, context=context)
