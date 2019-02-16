from app01 import models
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    """
    课程序例化
    """

    class Meta:
        model = models.CourseSubCategory
        fields = ['id', 'name']


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    课程详细序例化
    ps  不要在这类里面瞎写用没用,这是serializers配置类
        teachers 多对多老出bug,不能返回数据,不知道赖啥,
        多对多
    2018-11-12 17:52:43
    用了别人源码 写的代码一毛一样,就是我的获取不了数据,他的可以,
    难道,姿势不对?


    """
    # oto fenkey
    name = serializers.CharField(source='course.name')
    course_type = serializers.CharField(source='course.get_course_type_display')
    period = serializers.CharField(source='course.period')
    level = serializers.CharField(source='course.get_level_display')
    template_id = serializers.CharField(source='course.template_id')
    # mtm
    recommend_courses = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()
    courseoutlines = serializers.SerializerMethodField()
    oftenAskedquestions = serializers.SerializerMethodField()
    pricepolicy = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ['name', 'course_type', 'period', 'level', 'template_id', 'video_brief_link', 'why_study',
                  'what_to_study_brief', 'career_improvement', 'prerequisite', 'recommend_courses', 'teachers',
                  'courseoutlines', 'oftenAskedquestions', 'pricepolicy']

    def get_recommend_courses(self, obj):
        queryset = obj.recommend_courses.all()
        return [{'name': item.name} for item in queryset]

    def get_teachers(self, obj):
        queryset = obj.teachers.all()
        return [{'name': item.name, 'title': item.title, 'signature': item.signature, 'image': item.image,
                 'brief': item.brief, 'role': item.get_role_display()} for item in queryset]

    def get_courseoutlines(self, obj):
        queryset = obj.courseoutline_set.all()
        return [{'title': item.title, 'content': item.content} for item in queryset]

    def get_oftenAskedquestions(self, obj):
        queryset = obj.course.asked_question.all()
        return [{'question': item.question, 'answer': item.answer} for item in queryset]

    def get_pricepolicy(self, obj):
        queryset = obj.course.price_policy.all()
        return [{'price': item.price, 'valid_period': item.valid_period} for item in queryset]
