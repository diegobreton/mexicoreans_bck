from tastypie.resources import ModelResource
from api.models import Lesson, Level
from tastypie.authorization import Authorization

class LessonResource(ModelResource):
    class Meta:
        queryset = Lesson.objects.all()
        resource_name = 'lesson'
        authorization = Authorization()

class LevelResource(ModelResource):
    class Meta:
        queryset = Level.objects.all()
        resource_name = 'level'
        authorization = Authorization()
