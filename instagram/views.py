from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorOrReadonly
from .serializers import PostSerializer
from .models import Post


class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [IsAuthenticated]    # Django에서 사용
    permission_classes = [IsAuthenticated, IsAuthorOrReadonly]          # DRF에서 사용

    def perform_create(self, serializer):
        # FIXME: 인증이 되어있다는 가정하에, author를 지정해보겠슴.
        author = self.request.user  # User or AnonymousUser
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(ip=ip)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

#
# def post_list(request):
#     pass
#
# def post_detail(request, pk):
#     pass