from .models import Post
from rest_framework import generics
from .serializers import ListPostSerializer, CreatePostSerializer, UpdatePostSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated



class ListPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = ListPostSerializer
    permission_classes = (IsAuthenticated,)

class DetailPostView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = ListPostSerializer
    permission_classes = (IsAuthenticated,)

class CreatePostView(generics.CreateAPIView):
    serializer_class = CreatePostSerializer

class UpdatePostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = UpdatePostSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated,)