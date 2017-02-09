from django.conf.urls import url

from . import views

urlpatterns = [
    # mysite에서 보내준 url을 받아서 정규식으로 골라 post_list를 호출
    url(r'^post$', views.post_list, name='post_list'),
    # url에서 (?P<post_id>[0-9]+) 이 부분이 view의 post_detail 함수의 2번째 인자로 들어간다.
    # () 단위로 인자를 넘겨 줄 수 있다.() 그룹 하나당 인자 한개
    # post_id에 관한 테스트 :여기선 인자를 2개 넘겨준다. ([0-9]+), (\w+)
    # url(r'^post/([0-9]+)/(\w+)/', views.post_detail, name='post_detail'),
    # 하지만 여기선 (?P<name>expr) 패턴을 사용했기에,
    # post_detail함수의 매개변수의 이름과 같아야 정상 동작함.
    # url(r'^post/(?P<post_id>[0-9]+)/', views.post_detail, name='post_detail'),


    # name에 관해..예) name='post_detail'
    # 이 name을 이용해서 url 패턴을 템플릿이나 view에서 다시 사용할 수가 있다.
    # 그걸 ReverseMatch라고 한다.
    # 여기선 url패턴을 만들어 놨는데, templates에선 여기 이름을 이용해서 url 패턴을 만든다.(찾는다)
    # 이걸 ReverseMatch 하고 한다.

    # ReverseMatch
    url(r'^post/detail/(?P<post_id>[0-9]+)/', views.post_detail, name='post_detail'),
    # 여기서의 post_id가 키워드 인자값이 되어 template이나 view에서 ReverseMatch하는데 이용된다.
    # 여기서 키워드 인자 값을 보내주면, 여기 name을 이용해서 url패턴을 만들어 낸다.
]
