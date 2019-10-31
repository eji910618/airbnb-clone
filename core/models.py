from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    creeated = models.DateTimeField(auto_now_add=True)  # 생성날짜를 추가해줌
    updated = models.DateTimeField(auto_now=True)  # auto_now 새로운 날짜를 업데이트 해줌

    class Meta:
        abstract = True
