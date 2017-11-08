from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from posts.models import Post

from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    PostCreateUpdateSerializer,
    PostDetailSerializer,
    PostListSerializer
)

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    # lookup_url_kwarg = "abc"


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]
    # lookup_url_kwarg = "abc"

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        # email send_email


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    # lookup_url_kwarg = "abc"


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['title', 'content', 'user__first_name']
    pagination_class = PostLimitOffsetPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Post.objects.all() #filter(user=self.user.request)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()

        return queryset_list