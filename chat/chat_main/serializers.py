# from .models import *
# from rest_framework import serializers
#
#
# class ChatRoomSerializer(serializers.HyperlinkedModelSerializer):
#     # author = serializers.ReadOnlyField(source='author.username')
#     participants = serializers.PrimaryKeyRelatedField(many=True, queryset=Member.objects.all())
#
#     class Meta:
#         model = ChatRoom
#         fields = ['titles', 'author', 'participants', ]
#
#
# class MemberSerializer(serializers.HyperlinkedModelSerializer):
#     # chats = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = Member
#         fields = ['user', 'avatar', 'nickname', ]
