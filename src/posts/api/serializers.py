from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from comments.api.serializers import CommentListSerializer
from comments.models import Comment
from accounts.api.serializers import UserDetailSerializer

from posts.models import Post



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
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()

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
            'comments',
        ]
    
    def get_html(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        
        return image
    
    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentListSerializer(c_qs, many=True).data
        return comments

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
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
    
    # def get_user(self, obj):
    #     return str(obj.user.username)
