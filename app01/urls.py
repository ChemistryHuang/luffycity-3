from django.conf.urls import url

from app01.views import course, article, shoppingcar, payment


urlpatterns = [
    # 没有使用用户认证,所以不用login啦
    # url(r'^login/$', account.loginView.as_view()),
    # url(r'^course/$', course.CourseView.as_view()),
    # url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view()),

    # 方式二   用了请求方式对应方法这个方式
    # 关于课程的接口
    url(r'^course/$', course.CourseView.as_view({'get': 'list'})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get': 'retrieve'})),

    # 关于文章的接口
    url(r'^article/$', article.ArticleView.as_view({'get': 'list'})),
    url(r'^article/(?P<pk>\d+)/$', article.ArticleView.as_view({'get': 'retrieve'})),

    # 点赞的接口
    # url(r'^newspapers/(?P<pk>\d+)/agree/$', newspapers.AgreeView.as_view({'post': 'post'})),

    # 购物车接口
    # url(r'^shoppingcar/$', shoppingcar.ShoppingCarViewSet.as_view({'post': 'create','delete':'destroy',''})),
    url(r'^shoppingcar/$', shoppingcar.ShoppingCarViewSet.as_view()),

    # 结算中心接口
    url(r'^payment/$', payment.PaymentViewSet.as_view()),

    # 付钱的接口     由于是伪代码,自己弄
    # url(r'^order/$', order.OrderViewSet.as_view()),
]
