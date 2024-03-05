from rest_framework import serializers

from .models import Document, Question, Answer


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'user', 'file',)
        read_only_fields = ('user',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['file'] = instance.file.url
        return ret


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'user', 'document', 'question_text',)
        read_only_fields = ('user', 'document',)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'user', 'question', 'answer_text',)
        read_only_fields = ('user', 'question',)
