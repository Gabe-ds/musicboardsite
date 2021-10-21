from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm


# Create your views here.
# ログイン済みじゃないとsettings.pyのLOGIN_URLで設定されたページに飛ばされる
@login_required
def index(request):
    return render(request, 'musicboard/home.html')

class SignUpClass(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login_index')