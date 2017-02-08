"""
1. 파이선 셀에서 Post를 추가하고 저장해보기

    In [4]: p = Post(title='New Title', content = 'New Content')
    In [5]: p.save()
    이렇게 하면 save가 되지 않고 에러가 남.

    p = Post(title='New Title', content = 'New Content')
    from django.contrib.auth.models import User
    u = User.objects.first()
    p.author = u
    p.save()
    p.id 하면 6이 나옴(이유는 127.0.0.1:8000/admin에서 PostS 추가를 5개 했기 때문)

2. id가 2인 Post객체를 발행해보기
    p = Post.objects.get(id=2)
    p.publish()
    p.published_data
"""

from django.shortcuts import render

from .models import Post


# urls.py에서 호출되어 실행
def post_list(request):
    context = {
        # 객체를 넘겨줄 때는 '_'로 구분
        'post_list': Post.objects.all(),
    }
    return render(request, 'blog/post_list.html', context)
