from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from ..models import Post



class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            # 'slug',
            'content',
            'publish',
        ]

post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
)

class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'user',
            'slug',
            'content',
            'html',
            'publish',
            'image',
        ]
    
    def get_html(self, obj):
        return obj.get_markdown()
    
    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        
        return image

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    # delete_url = HyperlinkedIdentityField(
    #     view_name='posts-api:delete',
    #     lookup_field='slug'
    # )
    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'user',
            'content',
            # 'delete_url',
            'publish',
        ]
    
    def get_user(self, obj):
        return str(obj.user.username)
