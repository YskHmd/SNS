
from django.urls import path
from .views import signupfunc, loginfunc, listfunc

urlpatterns = [
    path('signup/',signupfunc, name='signup'),
    path('login/',loginfunc, name='login'),
    path('list/', listfunc, name='list'),
#reverseみたいに指定した名前から関数を呼び出すことができる
]