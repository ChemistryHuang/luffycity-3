
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from app01.models import *
from app01.utils.response import BaseResponse


class loginView(APIView):
    """
    用户登入
    """

    def post(self, request, *args, **kwargs):
        """
        用户认证
        :param request: 请求相关的数据
        :param args: URL传参
        :param kwargs: URL关键字传参
        :return:
        """
        # 实例化一个减少字典使用的类
        ret = BaseResponse()
        try:
            user = request.data.get('user')
            pwd = request.data.get('pwd')
            user = Account.objects.filter(username=user, password=pwd).first()
            if not user:
                ret.code = 1001
                ret.error = '用户名或密码错误'
                return Response(ret)
            uid = str(uuid.uuid4())
            UserAuthToken.objects.update_or_create(user=user, defaults={'token': uid})
            ret.data = uid
        except Exception as e:
            ret.code = 1003
        return Response(ret.dict)
