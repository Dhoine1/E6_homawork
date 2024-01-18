from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('chat/<int:pk>', views.ChatDetail.as_view()),
    # path('member/<int:pk>', views.MemberDetail.as_view()),
    path('<int:pk>/update/', ChatUpdate.as_view()),
    path('<int:pk>/delete/', ChatDelete.as_view()),
    path('create/', ChatCreate.as_view()),
    path('<int:pk>/chat/', chat, name='chat'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
