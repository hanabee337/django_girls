from django.http import HttpResponse


# urls.py에서 호출되어 실행
def post_list(request):
    return HttpResponse('post_list view')
