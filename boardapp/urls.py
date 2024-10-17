
from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc
from .views import BoardCreate, deletefunc, google_signup, google_login, download_link1, download_link2

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
    path('google_signup/', google_signup, name='google_signup'),
    path('download_link1/', download_link1, name='download_link1'),
    path('download_link2/', download_link2, name='download_link2'),

#reverseみたいに指定した名前から関数を呼び出すことができる
]