from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
)

from comments.models import Comment


class CommentListSerializer(ModelSerializer):
    # url = HyperlinkedIdentityField(
    #     view_name='comments-api:thread',
    #     lookup_field='pk'
    # )
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            # 'url',
            'content_type',
            'object_id',
            'parent',
            'content',
            'reply_count',
            'timestamp',
        ]
    
    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0


class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'timestamp',
        ]


class CommentDetailSerializer(ModelSerializer):
    replies = SerializerMethodField()
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'content',
            'reply_count',
            'replies',
            'timestamp',
        ]

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None
    
    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0