from django.shortcuts import render
from django.contrib.auth.models import User#ユーザー機能のライブラリ
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from .models import BoardModel
from django.contrib.auth.decorators import login_required




def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, ' ', password)#ユーザー保存先
            return render(request, 'signup.html', {'some':100})
        except IntegrityError:
                return render(request, 'signup.html', {'error':'このユーザーは既に登録されています'})
    return render(request, 'signup.html', {'some':100})

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
