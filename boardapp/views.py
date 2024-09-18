from django.shortcuts import render
from django.contrib.auth.models import User#ユーザー機能のライブラリ
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages  # メッセージフレームワークのインポート



def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            messages.success(request, 'ユーザー登録が完了しました。ログインしてください。')
            return redirect('login')  # ログインページにリダイレクト
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:#上の入力でユーザーがいる場合（NONEではない場合）
            login(request, user)
            return redirect('list')
        else:#いない場合
            return render(request, 'login.html', {'context':'Not logged in'})
    #とりあえずリダイレクトで返す文
    return render(request, 'login.html', {'context':'get method'})

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()#BoardModelのオブジェクトすべてをobject_list(変数)に入れることができる
    return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')
    # Redirect to a success page.

def detailfunc(request, pk):#urlsのpk 
    object = get_object_or_404(BoardModel, pk=pk)#右側のpkがurlsに行く
    return render(request, 'detail.html', {'object':object})
    #右側のobjectが1行上のobject（対象として持ってくるデータ）左がHTMLに表示する名前
    
def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)#get_object_or_404と意味は同じ
    object.good = object.good + 1 #押されたら１足す
    object.save()#それをセーブする
    return redirect('list')

def readfunc(request, pk):#初めては、押せる＋ユーザー名記録。押したことある人は何もしない、
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else:
        object.read = object.read + 1
        object.readtext = object.readtext + '' + username#同じ名前が来たらアウトなので本番不可
        object.save()#それをセーブする
        return redirect('list')
    
class BoardCreate(CreateView):#ClassBasedView
    template_name = 'create.html'
    model = BoardModel
    fields = ('content', 'sns_image')
    success_url = reverse_lazy('list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # 投稿者をログインユーザーに設定
        return super().form_valid(form)
    
@login_required
def deletefunc(request, pk):
    post = get_object_or_404(BoardModel, pk=pk)

    # 投稿者チェック
    if request.user.username == post.author:
        post.delete()
        return redirect('list')
    else:
        return redirect('detail', pk=pk)  # 投稿者でない場合、詳細ページに戻る
    