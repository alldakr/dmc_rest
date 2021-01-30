from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)  # 2개 url을 만들어줌

urlpatterns = [
    path('', include(router.urls)),
    path('public/', views.PublicPostListAPIView.as_view()),
]
