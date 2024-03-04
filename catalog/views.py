
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Document
from .serializers import DocumentSerializer


class DocumentCreateView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    # permission_classes = [IsAuthenticated,]


class UserDocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    # permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        queryset = Document.objects.filter(user=user)
        return queryset
