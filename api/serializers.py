from rest_framework import serializers
from .models import Questions,Answers,Tags

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ['pk', 'question', 'answer']

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Questions
        fields = ['pk', 'question','created']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ['pk', 'tag']