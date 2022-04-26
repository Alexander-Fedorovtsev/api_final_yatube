from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Post, Group, Comment, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )

    class Meta:
        model = Follow
        fields = "__all__"

    def create(self, validated_data):
        if self.is_valid():
            if validated_data["following"] == validated_data["user"]:
                raise serializers.ValidationError("На самого себя!")
            if Follow.objects.filter(**validated_data).exists():
                raise serializers.ValidationError(
                    "Такая подписка уже существует!"
                )
        return Follow.objects.create(**validated_data)
