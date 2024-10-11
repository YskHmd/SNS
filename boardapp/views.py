from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User#ユーザー機能のライブラリ
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # メッセージフレームワークのインポート
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from .models import BoardModel
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
import google.oauth2.id_token
import google.auth.transport.requests


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
    
@csrf_exempt
def google_login(request):
    if request.method == 'POST':
        id_token_str = request.POST.get('id_token')
        try:
            id_info = google.oauth2.id_token.verify_oauth2_token(
                id_token_str,
                google.auth.transport.requests.Request(),
                'YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com'
            )
            
            # ユーザー情報の取得
            email = id_info.get('email')
            name = id_info.get('name')
            picture = id_info.get('picture')
            
            # ユーザーの作成または取得
            user, created = User.objects.get_or_create(username=email, email=email)
            if created:
                user.first_name = name
                user.save()
            
            # ログイン
            login(request, user)
            return redirect('home')  # ログイン後のリダイレクト先
            
        except ValueError:
            # 無効なトークン
            return redirect('login')  # エラーメッセージを表示することを推奨
    
    return redirect('login')