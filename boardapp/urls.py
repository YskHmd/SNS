
from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc

urlpatterns = [
    path('signup/',signupfunc, name='signup'),
    path('login/',loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name = 'logout'),
    path('detail/<int:pk>', detailfunc, name = 'detail')
#reverseみたいに指定した名前から関数を呼び出すことができる
]