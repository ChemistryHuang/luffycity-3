from app01 import models
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    """
    文章序例化
    """
    source = serializers.CharField(source="source.name")
    article_type = serializers.CharField(source="get_article_type_display")
    position = serializers.CharField(source='get_position_display')

    class Meta:
        model = models.Article
        fields = ["title", "source", "article_type", 'head_img', 'brief', 'pub_date', 'comment_num', 'agree_num',
                  'view_num', 'collect_num', 'position']


class ArticleDetailViewSetSerializers(serializers.ModelSerializer):
    """
    文章详细序例化
    """
    class Meta:
        model = models.Article
        fields = ['title', 'pub_date', 'agree_num', 'view_num', 'collect_num', 'comment_num', 'source', 'content',
                  'head_img']
