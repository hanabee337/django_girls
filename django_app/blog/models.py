from django.db import models
from django.utils import timezone


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
