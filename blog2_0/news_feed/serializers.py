from rest_framework.serializers import ModelSerializer
from .models import Page, Post


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostPageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"

    def to_representation(self, instance):
        if isinstance(instance, Page):
            serializer = PageSerializer(instance)
            return serializer.data
        elif isinstance(instance, Post):
            serializer = PostSerializer(instance)
            return serializer.data

