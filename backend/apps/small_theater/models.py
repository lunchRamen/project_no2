from django.db import models


# Create your models here.
class SmallTheater(models.Model):
    published_date = models.DateField()
    title = models.CharField(max_length=200, default="")
    theater_owner = models.CharField(max_length=10, null=True)
    theater_genre1 = models.CharField(
        max_length=30, null=True
    )  # 'action' / default=''할까
    theater_genre2 = models.CharField(max_length=30, null=True)
    introduce = models.CharField(max_length=1000, null=True)
    notice = models.CharField(max_length=1000, null=True)

    class Meta:
        # managed = False # 자동 migration
        db_table = "small_theater"
