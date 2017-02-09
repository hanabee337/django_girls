from django.conf.urls import url

from . import views

urlpatterns = [
    # mysite에서 보내준 url을 받아서 정규식으로 골라 post_list를 호출
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<post_id>[0-9]+)/', views.post_detail, name='post_detail'),
]
