from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, CreateView, DeleteView
from .models import *
from . import serializers
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse_lazy


# стартовая страница. Проверяет зарегистрирован ли пользователь. Выводит его чаты и список всех юзеров.
def index(request):
    if request.user.is_authenticated:
        member_of_chat = []
        chats = ChatRoom.objects.filter(author=request.user)
        all_users = Member.objects.all()
        for somebody in ChatRoom.objects.all():
            for i in somebody.participants.all():
                if request.user == i.user and request.user != somebody.author:
                    member_of_chat.append(somebody.pk)

        another_chat = ChatRoom.objects.filter(pk__in=member_of_chat)
        return render(request, 'index.html', {'all_users': all_users,
                                              'chats': chats,
                                              'another_chat': another_chat,
                                              })
    else:
        return render(request, 'notlogin.html')


# профиль пользователя
def profile(request):
    return render(request, "profile.html")


# редактирование своего профиля. ник и ава
class ProfileUpdate(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    model = Member
    template_name = 'profileupdate.html'
    raise_exception = True
    success_url = reverse_lazy('profile')


# создание профиля для зарегистрированого юзера
class ProfileCreate(LoginRequiredMixin, CreateView):
    form_class = ProfileForm
    model = Member
    template_name = 'profileupdate.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('profile')


# создание массового чата
class ChatCreate(LoginRequiredMixin, CreateView):
    form_class = ChatForm
    model = ChatRoom
    template_name = 'chatupdate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('index')


# редактирование чата
class ChatUpdate(LoginRequiredMixin, UpdateView):
    form_class = ChatForm
    model = ChatRoom
    template_name = 'chatupdate.html'
    raise_exception = True
    success_url = reverse_lazy('index')


# удаление чата
class ChatDelete(LoginRequiredMixin, DeleteView):
    model = ChatRoom
    template_name = 'chatdelete.html'
    success_url = reverse_lazy('index')
    raise_exception = True


# комната чата
def chat(request, **kwargs):
    return render(request, "chatdetail.html")


# просмотр профиля другого юзера с возможностью создать с ним чат
@login_required
def profiledetailview(request, pk, **kwargs):
    member = Member.objects.filter(pk__exact=pk)
    for one in member:
        member_nik = one.nickname
        member_ava = one.avatar.url

    user_profile = get_object_or_404(Member, id=pk)
    if user_profile.user.id == request.user.id:
        show = 0
    else:
        show = 1

    if request.method == "POST":
        new_chat = ChatRoom()
        new_chat.titles = request.POST.get("text")
        new_chat.author = request.user
        new_chat.save()
        new_chat.participants.set(member)

        return render(request, 'success.html', {'member_nik': member_nik,
                                                'chat_name': new_chat.titles})

    return render(request, 'profiledetailview.html', {'member_nik': member_nik,
                                                      'member_ava': member_ava,
                                                      'show': show, })
