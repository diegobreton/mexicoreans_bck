from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.
class Lesson(models.Model):
    author = models.CharField(max_length=25)
    body = models.TextField()
    code = models.CharField(max_length=8)
    lessonId = models.AutoField(primary_key=True)
    level = models.SmallIntegerField(default=99)
    modifiedDate = models.DateTimeField()
    thumbnailImgUrl = models.URLField()
    title = models.TextField()
    uploadedDate = models.DateTimeField()

    def __str__(self):
        return "%s -- %s: %s" % (self.lessonId, self.code, self.title)

class Level(models.Model):
    levelId = models.SmallIntegerField(primary_key=True)
    body = models.TextField()
    thumbnailImgUrl = models.URLField()
    lessonCollection = models.CharField(max_length = 150, validators=[validate_comma_separated_integer_list])
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Level %s" % (self.levelId)
