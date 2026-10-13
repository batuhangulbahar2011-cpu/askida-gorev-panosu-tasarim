from django.urls import path
from . import views
urlpatterns = [
    path('', views.board, name='board'), path('giris/', views.sign_in, name='login'), path('cikis/', views.sign_out, name='logout'),
    path('kayit/', views.register, name='register'), path('parola-yenile/', views.reset_password, name='reset'),
    path('istek/yeni/', views.create_request, name='create'), path('istek/<int:pk>/', views.detail, name='detail'),
    path('istek/<int:pk>/duzenle/', views.edit_request, name='edit'), path('istek/<int:pk>/islem/', views.action, name='action'),
    path('arsiv/', views.archive, name='archive'), path('bildirimler/', views.notifications, name='notifications'),
    path('bildirim/<int:pk>/oku/', views.read_notification, name='read_notification'),
    path('danisman/', views.summary, name='summary'), path('takim/', views.team, name='team'),
]
