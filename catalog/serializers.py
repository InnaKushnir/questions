from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'user', 'file',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['file'] = instance.file.url
        return ret