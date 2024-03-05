from django.urls import path

from catalog.views import DocumentCreateView, UserDocumentListView, DocumentDetailView, QuestionCreateView, \
    AnswerCreateView

urlpatterns = [
    path('documents/create/', DocumentCreateView.as_view(), name='document-create'),
    path('documents/', UserDocumentListView.as_view(), name='document-list'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('documents/<int:pk>/question/create/', QuestionCreateView.as_view(), name='question-create'),
    path('answers/create/<int:question_pk>/', AnswerCreateView.as_view(), name='answer-create'),
]

app_name = "catalog"
