from rest_framework import serializers
from .models import Blog,BlogTag,BlogType,Comment

class BlogListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        extra_kwargs = {  # 对模型已有参数重新设置和编辑
            'pbtime': {'required': False, 'read_only': True}  # 可以不填   read_only 不显示该字段
        }

class BlogTypeSerializer1(serializers.ModelSerializer):

    class Meta:
        model = BlogType
        fields = "__all__"

class BlogTypeSerializer2(serializers.ModelSerializer):
    sonm = BlogTypeSerializer1(many=True)
    class Meta:
        model = BlogType
        fields = "__all__"

class BlogTypeSerializer3(serializers.ModelSerializer):
    sonm = BlogTypeSerializer2(many=True) #  models 外键设置属性related_name=son
    class Meta:
        model = BlogType
        fields = "__all__"

class CommentListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {  # 对模型已有参数重新设置和编辑
            'pbtime': {'required': False, 'read_only': True}  # 可以不填   read_only 不显示该字段
        }
