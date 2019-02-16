
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app01.models import *


class LuffyAuth(BaseAuthentication):
    """
    用户认证类
    """
    def authenticate(self, request):
        """
        用户认证
        :param request:
        :return:
        """
        # http://wwwww...c0ovmadfasd/?token=adfasdfasdf
        token = request.query_params.get('token')
        obj = UserAuthToken.objects.filter(token=token).first()
        if not obj:
            return AuthenticationFailed({'code': 1001, 'erroe': '认证失败'})
        return (obj.user.username, obj)

