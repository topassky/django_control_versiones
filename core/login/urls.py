from django.urls import path, include
from core.login.views import LoginFormView2, LoginFormView, LogoutView, LagoutRedirecView

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logoutview'),
    path('logout/', LagoutRedirecView.as_view(), name='logoutview')
]
