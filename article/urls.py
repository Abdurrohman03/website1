from django.urls import path
from .views import index, detail
app_name = 'article'

urlpatterns = [
    path('', index, name='list'),
    path('article/<int:pk>/', detail, name='detail')
]
