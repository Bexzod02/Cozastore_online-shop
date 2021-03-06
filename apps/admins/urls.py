from django.urls import path
from .views import login_view, logout_view, registration_view
app_name = 'admins'

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registration_view, name='register'),
]
