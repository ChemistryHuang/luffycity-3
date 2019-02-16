from rest_framework.views import APIView
from app01.serializers.course import CourseSerializer, CourseDetailSerializer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from app01 import models


class CourseView(ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            queryset = models.CourseSubCategory.objects.all()
            ser = CourseSerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}

        try:
            # 课程ID=2
            pk = kwargs.get('pk')
            # 课程详细对象
            obj = models.CourseDetail.objects.filter(course_id=pk).first()
            ser = CourseDetailSerializer(instance=obj, many=False)
            ret['data'] = ser.data
            print( ret['data'])
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)