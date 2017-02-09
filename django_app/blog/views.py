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

3. post_list에 빈 리스트가 전달될 경우, 템플릿에서 포스트 없음을 출력
   테스트는 127.0.0.1:8000/admin에서 Posts에 올린 것들 모두,
    시간 설정을 없애면 post_list.html templates에서 포스트 없음이 출력되는지
    확인해 볼 수 있다.

Detail View를 만들어 봅니다.
    1. View에 post_detail 함수 추가
        post_detail은 인자로 post_id를 받는다.
    2. urls.py에 해당 view와 연결하는 url을 추가
        정규식표현으로 패턴네임 post_id 이름을 갖는 숫자 1개이상의 패턴을 등록
    3. post_detail 뷰가 원하는 URL에서 잘 출력되는지 확인 후(stub 메서드 사용)
        get 퀴리셋을 사용해서 (Post.objects.get(...))
        id 값이 인자로 전달된 post_id 와 같은 Post 객체를 context에 담아
        post-detail.html을 render 한 결과를 리턴
    4. 템플릿에 post-detail.html을 만들고,
        인자로 전달된 Post 객체에 title, content, created_data, published_data 출력
"""
from django.shortcuts import render

from .models import Post


# urls.py에서 호출되어 실행
def post_list(request):
    context = {
        #     # 객체를 넘겨줄 때는 '_'로 구분
        #     'post_list': Post.objects.filter(
        #         published_data__lte=timezone.now())
        'post_list': Post.objects.all()

    }
    return render(request, 'blog/post_list.html', context)


# post_id에 관해...
# post_detail 함수의 2번째 인자인 post_id는 urls.py에서 넘어온 인자인데,
# 여기서 post_id라는 인자는 임의의 이름이다. 따라서, 다른 이름으로 해도 상관없다.
# urls.py의 url이 넘져주는 인자의 갯수와 post_detail함수의 인자 갯수와 같아야 한다.
# post_id에 관한 테스트.
# def post_detail(request, pst, any_str):
# return HttpResponse('post_detail, post_id: {}, any_str:{}'.format(pst, any_str))
def post_detail(request, post_id):
    # ORM을 이용해서 id가 전달받은 post_id와 일치하는 Post객체를 post변수에 전달
    post = Post.objects.get(id=post_id)
    # 전달할 context 딕셔너리의 키 'post_detail'에 post변수를 전달
    context = {
        # 'post_detail' 이 이름이 post-detail.html의 post_detail과 동일한 이름을 가져야 한다.
        # 즉, post_detail함수에서는 context 딕셔너리 키 값 'post-detail'을
        # post-detail.html templates에 리턴해준다
        'post_detail': post
    }
    # blog/post-detail.html 템플릿을 render한 결과를 리턴
    return render(request, 'blog/post-detail.html', context)
