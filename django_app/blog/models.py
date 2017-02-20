from django.db import models
from django.utils import timezone
"""
1. 모델을 정의
2. 모델이 속한 app을 settings.py의 INSTALLED_APPS에 등록
3. 등록 후 해당 app의 모델을 데이터베이스에 적용시키기위해 makemigrations -> migrate
4. 장고 어드민에 등록시킬 모델을 admin.py에 admin.site.register(모델명)으로 등록
5. 장고 어드민에 로그인 하기위해 ./manage.py createsuperuser로 관리자계정 생성
6. runserver후 localhost:8000/admin으로 접속해서 해당 계정으로 로그인
7. person앱의 Person테이블이 잘 보이는지 확인
"""

# Table로 정의될 Class를 models.Model이 Django통해서 Table을 만들어 준다.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    published_data = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        # 실행시, 해당 인스턴스의 published_data에 현재시간을 기록하고
        # DB에 업데이트 한다.
        self.published_data = timezone.now()
        self.save()
