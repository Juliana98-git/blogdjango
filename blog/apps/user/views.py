from django.shortcuts import render
from django.views.generic import TemplateView

# TODO: Cambiar TemplateView por DetailView para que se pueda ver el detalle de un
# perfil de usuario

class UserProfileView(TemplateView):
    template_name = 'user/user_profile.html'
