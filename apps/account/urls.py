from django.urls import path
from django.contrib.auth import views as auth_view
from .views import registration_view
app_name = 'accounts'

urlpatterns = [
    path('/registers/', registration_view),
    # path('logins/', auth_view.LoginView.as_view(template_name='login.html'), name='logins'),
    # path('logout/', auth_view.LogoutView.as_view(), name='logout'),
]