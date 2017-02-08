# urls.py에서 호출되어 실행
from django.shortcuts import render

from .models import Post


def post_list(request):
    context = {
        # 객체를 넘겨줄 때는 '_'로 구분
        'post_list': Post.objects.all(),
    }
    return render(request, 'blog/post_list.html', context)
