from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from rest_framework.response import Response
from django_redis import get_redis_connection
from app01.utils.response import BaseResponse
from app01.utils.auth import LuffyAuth
from app01 import models
from django.core.exceptions import ObjectDoesNotExist
from app01.utils.exception import PricePolicyInvalid
from django.conf import settings
import json


class ShoppingCarViewSet(APIView):
    authentication_classes = [LuffyAuth, ]
    conn = get_redis_connection("default")  # 类下的全局 下面用加self

    def post(self, request, *args, **kwargs):
        """
        将课程添加到购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()
        try:
            # 1. 获取用户提交的课程ID和价格策略ID
            course_id = int(request.data.get('courseid'))
            policy_id = int(request.data.get('policyid'))

            # 2. 获取专题课信息
            course = models.Course.objects.get(id=course_id)

            # 3. 获取该课程相关的所有价格策略
            price_policy_list = course.price_policy.all()
            price_policy_dict = {}
            for item in price_policy_list:
                price_policy_dict[item.id] = {
                    "period": item.valid_period,
                    "period_display": item.get_valid_period_display(),
                    "price": item.price,
                }

            # 4. 判断用户提交的价格策略是否合法
            if policy_id not in price_policy_dict:
                # 价格策略不合法
                raise PricePolicyInvalid('价格策略不合法')

            # 5. 将购物信息添加到redis中
            # self.conn
            # car_key = "luffy_shopping_car_%s_%s"
            car_key = settings.SHOPPING_CAR_KEY % (request.auth.user_id, course_id,)
            car_dict = {
                'title': course.name,
                'img': course.course_img,
                'default_policy': policy_id,
                'policy': json.dumps(price_policy_dict)
            }
            # conn = get_redis_connection("default")
            self.conn.hmset(car_key, car_dict)
            ret.data = '添加成功'

        except PricePolicyInvalid as e:
            ret.code = 2001
            ret.error = e.msg
        except ObjectDoesNotExist as e:
            ret.code = 2001
            ret.error = '课程不存在'
        except Exception as e:
            ret.code = 1001
            ret.error = '获取购物车失败'
        return Response(ret.dict)

    def delete(self, request, *args, **kwargs):
        """
        购物车中删除课程
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()
        try:
            course_id_list = request.data.get('courseids')
            key_list = [settings.SHOPPING_CAR_KEY % (request.auth.user_id, course_id,) for course_id in course_id_list]
            self.conn.delete(*key_list)
        except Exception as e:
            ret.code = 1002
            ret.error = "删除失败"

        return Response(ret.dict)

    def patch(self, request, *args, **kwargs):
        """
        修改课程的价格策略
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()
        try:
            # 1. 获取价格策略ID和课程ID
            course_id = int(request.data.get('courseid'))
            policy_id = str(request.data.get('policyid'))

            # 2. 拼接课程的key
            key = settings.SHOPPING_CAR_KEY % (request.auth.user_id, course_id,)
            if not self.conn.exists(key):
                ret.code = 1002
                ret.error = "购物车中不存在此课程"
                return Response(ret.dict)
            # 3. redis中获取所有的价格策略
            policy_dict = json.loads(str(self.conn.hget(key, 'policy'), encoding='utf-8'))
            if policy_id not in policy_dict:
                ret.code = 1003
                ret.error = "价格策略不合法"
                return Response(ret.dict)

            # 4. 在购物车中修改该课程的默认价格策略
            self.conn.hset(key, 'default_policy', policy_id)

            ret.data = "修改成功"

        except Exception as e:
            ret.code = 1004
            ret.error = "修改失败"

        return Response(ret.dict)

    def get(self, request, *args, **kwargs):
        """
        查看购物车中所有的商品
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()
        try:
            key_match = settings.SHOPPING_CAR_KEY % (request.auth.user_id, "*")

            course_list = []

            for key in self.conn.scan_iter(key_match, count=10):
                info = {
                    "title": self.conn.hget(key, 'title').decode('utf-8'),
                    "img": self.conn.hget(key, 'img').decode('utf-8'),
                    "policy": json.loads(self.conn.hget(key, 'policy').decode('utf-8')),
                    "default_policy": self.conn.hget(key, 'default_policy').decode('utf-8')
                }
                course_list.append(info)
            ret.data = course_list
        except Exception as e:
            ret.code = 1002
            ret.error = "获取失败"
        return Response(ret.dict)


class ShoppingCarDetailViewSet(ViewSetMixin, APIView):

    def retrieve(self, request, *args, **kwargs):
        """
        查一条
        """
        ret = {'code': 1000, 'data': None}

        try:
            pass
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程详细失败'
        return Response(ret)

    '''
    缺
    
    删 delete
    改 put
    
    一条
    
    '''
