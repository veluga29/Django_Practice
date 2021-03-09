from django.db import models


# Create your models here.
class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add는 record가 db로 삽입될 때의 시각 기록
    updated_at = models.DateTimeField(auto_now=True)  # auto_now는 모델을 통해 저장할 때의 수정 시각을 기록

    # JAVA의 toString()과 유사하게 파이썬에서 어떤 객체에 대해 문자열로 표현하는 법
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        # return "Custom Post object ({})".format(self.id)
        return self.message

    # def message_length(self):  # 자주 쓰이면 model에 쓰면되지만, admin에서만 쓰인다면 admin에서 써도 됨
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"
