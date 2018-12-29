
from django.urls import path
from .views import TalkCreateView, TalkDetailView


urlpatterns = [
    # 一覧画面
    path('', TalkDetailView.as_view(), name='index'),
    # 登録画面
    path('create/', TalkCreateView.as_view(), name='create'),


]