from django.db import models
from django.utils import timezone


# Table로 정의될 Class를 models.Model이 Django통해서 Table을 만들어 준다.
class Post(models.Model):
    # 저자 : 외래키로 연결 (auth 어플리케이션의 User 모델)
    author = models.ForeignKey('auth.User')
    # 제목 , 길이 제한 텍스트
    title = models.CharField(max_length=200)
    # 내용 : 길이 제한 없는 텍스트
    content = models.TextField()
    # 생성일자 : auto_now_add 이용해서 객체가 생성될 떄의 시간을 자동으로 기록
    created_date = models.DateTimeField(auto_now_add=True)
    # 발행일자, 없는 값(null)을 허용해준다
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        # 실행시, 해당 인스턴스의 published_data에 현재시간을 기록하고
        # DB에 업데이트 한다.
        self.published_data = timezone.now()
        self.save()
