from django.conf.urls import url

from . import views

urlpatterns = [
    # mysite에서 보내준 url을 받아서 정규식으로 골라 post_list를 호출
    url(r'^$', views.post_list, name='post_list'),
]
