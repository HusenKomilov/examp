from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    title = models.CharField(max_length=128)
    buy_user = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    title = models.CharField(max_length=128)
    course = models.ManyToManyField(Course)
    video_url = models.URLField()
    total_time = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class LessonUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    watched = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def is_finesh(self):
        return (self.watched * 100) / self.total >= 80

    @property
    def status(self):
        if self.is_finesh():
            return "Tugadi"
        elif self.watched > 0:
            return "Jarayonda"
        elif self.watched == 0:
            return "O'tmadi"


class LessonWatched(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    from_time = models.IntegerField(default=0)
    to_time = models.IntegerField(default=0)
