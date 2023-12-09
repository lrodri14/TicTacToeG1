from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import JugadorAuthCreationForm
from .models import Record
# Create your views here.


class SignUp(View):

    template_name = 'autenticacion/sign-up.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password1')
        created_user = JugadorAuthCreationForm(request.POST)
        if created_user.is_valid():
            user = created_user.save()
            Record.objects.create(jugador=user)
            auth_user = authenticate(request, username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('menu:menu')
        else:
            context = {'error': 'Algunos campos no coinciden'}
            return render(request, self.template_name, context=context)


class Login(View):

    template_name = 'autenticacion/sign-in.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu:menu')
        else:
            context = {'error': 'Por favor asegure que sus credenciales sean las correctas'}
            return render(request, self.template_name, context=context)


class Logout(View):

    template_name = 'autenticacion/sign-in.html'

    def get(self, request):
        logout(request)
        return render(request, self.template_name)

