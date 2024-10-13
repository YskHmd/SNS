
from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc
from .views import BoardCreate, deletefunc, google_login, download_resume

urlpatterns = [
    path('', loginfunc, name='home'),  # とりあえずログイン
    path('signup/',signupfunc, name='signup'),
    path('login/',loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name = 'logout'),
    path('detail/<int:pk>', detailfunc, name = 'detail'),
    path('good/<int:pk>', goodfunc, name = 'good'),
    path('read/<int:pk>', readfunc, name = 'read'),
    path('create/', BoardCreate.as_view(), name = 'create'),
    path('delete/<int:pk>/', deletefunc, name='delete'),
    path('accounts/google/login/callback/', google_login, name='google_login'),
    path('download_resume/', download_resume, name='download_resume'),
#reverseみたいに指定した名前から関数を呼び出すことができる
]