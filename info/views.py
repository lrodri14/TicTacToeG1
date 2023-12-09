from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class Info(View):
    template_name = 'info/info.html'

    def get(self, request):
        return render(request, self.template_name)
