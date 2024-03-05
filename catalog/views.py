import os

from django.shortcuts import get_object_or_404
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFium2Loader
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Document, Question
from .serializers import DocumentSerializer, QuestionSerializer, AnswerSerializer

os.environ["OPENAI_API_KEY"] = "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"


class DocumentCreateView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserDocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        queryset = Document.objects.filter(user=user)
        return queryset


class DocumentDetailView(generics.RetrieveAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        queryset = Document.objects.filter(user=user)
        return queryset


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        document_id = self.kwargs.get('pk')
        document = get_object_or_404(Document, pk=document_id)

        serializer.save(user=self.request.user, document=document)

        question = serializer.instance

        return Response({'question_id': question.id}, status=status.HTTP_201_CREATED)


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            question_pk = self.request.data.get('question_id')
            question_ = get_object_or_404(Question, pk=question_pk)

            file_path = question_.document.file.path
            pdf_loader = PyPDFium2Loader(file_path)
            documents = pdf_loader.load()

            chain = load_qa_chain(llm=ChatOpenAI(model_name='gpt-3.5-turbo'))
            query = question_.question_text
            response_ = chain.run(input_documents=documents, question=query)

            serializer.save(user=self.request.user, question=question_, answer_text=response_)

            return Response({'answer': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
