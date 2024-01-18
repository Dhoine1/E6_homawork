from django.db import models
from django.contrib.auth.models import User


# модель профиля
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    nickname = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nickname}'


# модель чата
class ChatRoom(models.Model):
    titles = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Member, related_name='chats')

    def __str__(self):
        return f'{self.titles}. Автор: {self.author}'
