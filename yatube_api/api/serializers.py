from rest_framework import serializers

from posts.models import Post, Group, User, Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    group = serializers.SlugRelatedField(slug_field='slug',
                                         queryset=Group.objects.all(), required=False)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')
