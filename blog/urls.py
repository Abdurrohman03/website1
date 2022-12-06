from django.urls import path
from .views import index, detail
app_name = 'blog'

urlpatterns = [
    path('blog/', index, name='list'),
    path('blog/<int:pk>/', detail, name='detail')
]
