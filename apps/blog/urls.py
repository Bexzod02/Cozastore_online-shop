from django.urls import path
from .views import blog_view, blog_detail
app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('bdetail/<int:pk>/', blog_detail, name='bdetail')
]