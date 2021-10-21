from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .models import *


# ログイン済みじゃないとsettings.pyのLOGIN_URLで設定されたページに飛ばされる
# url.pyのas_view()が@login_requiredがあると使えない
@method_decorator(login_required, name='dispatch')
class HomeClass(ListView):
    template_name = 'musicboard/home.html'
    model = BoardModel
    # id新しい順に並び替え
    ordering = ['-id']
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # idが新しい順に並び替えて最新5件を取得
        context['data_list'] = PosterModel.objects.all().order_by('-id')[0:5]
        
        return context

@method_decorator(login_required, name='dispatch')
class CreateClass(CreateView):
    template_name = 'musicboard/create.html'
    model = BoardModel
    fields = ('category', 'song', 'artist', 'music', 'subtitle')
    success_url = reverse_lazy('home')
    
@method_decorator(login_required, name='dispatch')
class DetailClass(DetailView):
    template_name = 'musicboard/detail.html'
    model = BoardModel
    # 引き継ぎがうまくいかなかったので定義してあげる
    context_object_name = 'detail'
    
    # 上で指定したモデルとは別のモデルから取り出して，データをリストで取得するためのもの
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # urls.pyで指定しているpkを受け渡してフィルターにかけている(`self.kwargs.get('pk')`)
        # https://stackoverflow.com/questions/21758731/how-can-i-get-pk-or-id-in-get-context-data-from-cbv
        # https://qiita.com/sr2460/items/ec864cb6457016ec8c14
        context['data_list'] = PosterModel.objects.filter(board_id=self.kwargs.get('pk'))
        
        return context

@method_decorator(login_required, name='dispatch')
class PostClass(LoginRequiredMixin, CreateView):
    template_name = 'musicboard/post.html'
    model = PosterModel
    fields = ('board', 'content',)
    success_url = reverse_lazy('home')
    
    # ログインしているユーザー名で投稿者に格納するためのもの
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)