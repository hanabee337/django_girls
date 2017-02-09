from django.conf.urls import url

from . import views

urlpatterns = [
    # mysite에서 보내준 url을 받아서 정규식으로 골라 post_list를 호출
    url(r'^$', views.post_list, name='post_list'),
    # url에서 (?P<post_id>[0-9]+) 이 부분이 view의 post_detail 함수의 2번째 인자로 들어간다.
    # () 단위로 인자를 넘겨 줄 수 있다.() 그룹 하나당 인자 한개
    # post_id에 관한 테스트 :여기선 인자를 2개 넘겨준다. ([0-9]+), (\w+)
    url(r'^post/([0-9]+)/(\w+)/', views.post_detail, name='post_detail'),

    # 하지만 여기선 (?P<name>expr) 패턴을 사용했기에,
    # post_detail함수의 매개변수의 이름과 같아야 정상 동작함.
    # url(r'^post/(?P<post_id>[0-9]+)/', views.post_detail, name='post_detail'),
]
