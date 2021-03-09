from django.db import models


# Create your models here.
class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add는 record가 db로 삽입될 때의 시각 기록
    updated_at = models.DateTimeField(auto_now=True)  # auto_now는 모델을 통해 저장할 때의 수정 시각을 기록
