from django.urls import path
from core.user.views import  UserView

urlpatterns = [
    path('', UserView.as_view(), name='user_template')
    #path('', UserCreateView.as_view(), name='user_template')
]