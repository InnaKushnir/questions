from django.urls import path

from catalog.views import DocumentCreateView, UserDocumentListView

urlpatterns = [
    path('documents/create/', DocumentCreateView.as_view(), name='document-create'),
    path('documents/', UserDocumentListView.as_view(), name='document-list'),
    ]

app_name = "catalog"
