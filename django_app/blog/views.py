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
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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
    # Error Handling (1)
    # try:
    #     # ORM을 이용해서 id가 전달받은 post_id와 일치하는 Post객체를 post변수에 전달
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist as e:
    #     # DoesNotExist 예외 발생시 해당 예외를 리턴
    #     return HttpResponse(e)

    # Error Handling (2)
    # 어떤 경우에는 해당 객체에 대한 pk 즉, id가 없는 경우가 있다.
    # 이런 경우에도 대응할 수 있는 좀 편하게 쓸 수 있는 방법이
    post = get_object_or_404(Post, id=post_id)

    # 전달할 context 딕셔너리의 키 'post_detail'에 post변수를 전달
    context = {
        # 'post_detail' 이 이름이 post-detail.html의 post_detail과 동일한 이름을 가져야 한다.
        # 즉, post_detail함수에서는 context 딕셔너리 키 값 'post-detail'을
        # post-detail.html templates에 리턴해준다
        'post_detail': post
    }
    # blog/post-detail.html 템플릿을 render한 결과를 리턴
    return render(request, 'blog/post-detail.html', context)




# Mission :
# 1. view
#     def post_add(request)
# 2. url
#     post/add/, name='post_add'
# 3. 상기 조건에 맞게 view와 url을 작성한 다음,
#     post-add.html이랑 연결을 해보자.
# 4. post_list.html에서 'Write Post' 버튼을 만들고,
#  해당 버튼에 post_add로 가는 링크 생성
def post_add(request):

    # 요청의 method가 POST인 경우,
    # 요청받은 데이터 출력
    if request.method == 'POST':
        print(request.POST)
        # request.POST는 딕셔너리 형태
        data = request.POST
        # 'input_title' 과 'input_content'는 키 값인데,
        # 어디서 만들어졌냐?하면,
        # post-add.html의 input/textarea 요소의 name으로 데이터의 키 값을 만들었다.
        # 그래서, 만약에 post-add.html에서 해당 요소의 name을 바꾸면,
        # 여기서도 거기에 맞게 수정해야 한다.
        title = data['input_title']
        content = data['input_content']
        author = User.objects.get(id=1)
        print(title, content, author)
        ret = ','.join([title, content])
        # return HttpResponse(ret)

        # 지금 조건에서 http://127.0.0.1:8000/post/add/ 로 접속하면 하기와 같은 에러가 발생함.
        # MultiValueDictKeyError
        # at  /post/add/
        # "'input_title'"
        # 이유는 request.POST를 가져왔는데, 그 안에 'input_title'이 있어서,
        # 에러가 난 것임
        # 해결 방법 : 한 페이지 안에서 페이지를 보여주는 것과 데이터를 받아서 처리하는 것을
        # request의 method에 따라 처리를 달리 해줘야 함.


        # Mission : 받은 데이터를 사용해서 Post 객체 생성
        #'Post created' 메세지 출력
        p = Post(title=title, content=content, author=author)
        p.save()
        # return HttpResponse('Post created')
        # 위의 Post나 밑의 objects.create나 Post 객체를 만드는 것은 동일함.
        # 그러나, Post로 하면 save까지 해줘야 함. create으로 하면, save까지 해줌
        # Post.objects.create(title=title, content=content, author=author)

        # redirect('/post')라고 입력하면 하드 코딩(고정된 URL)이라, 비효율적임.
        # 따라서, 하기와 같이 동적으로 입력하기 위해선,
        # URL 패턴의 name을 입력해야 하는데,
        # 이 때, redirect는 받은 인자를 확인해보니,
        # URL이 아니므로, 이 인자(여기선 name)를 urls.py에서 찾음.
        # 이름을 갖고 찾은 url로 가라고 browser에게 전달함.
        return redirect('post_list')
        # redirect 메서드는 인자로 주어진
        # URL 또는
        # urlpatterns의 name을 이용해 만들어낸 URL을 사용해서
        # 브라우저가 해당 URL로 이동하도록 해줌.

    # 요청의 method가 POST가 아닌 경우,
    # 글 쓰기 양식이 있는 템플릿을 렌더해서 리턴
    else:
        # request의 method에 따른 방법. 여기서는 페이지를 보여주는 부분
        return render(request, 'blog/post-add.html')
