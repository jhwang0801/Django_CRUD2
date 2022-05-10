from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age = models.IntegerField()

    class Meta:
        db_table = 'owners'


class Dog(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField(default=0)
    owner = models.ForeignKey("Owner", on_delete=models.CASCADE)

    # 자세히 다 짚고 넘어가자...ForeginKey 필드 관련,
    # models.ForeignKey('self', on_delete=models.CASCADE) //
    # class ForeignKey(to, on_delete, **options)라고 알고 있다.
    # 그러면 위에 해당 필드에서의 "Owner"가 가르키는 것은 위에 할당해 준 Owner Class인가?
    # 아니면 다른 무엇인가?

    class Meta:
        db_table = 'dogs'