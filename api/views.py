
from .models import Questions,Answers,Tags
from rest_framework import generics
from .serializers import QuestionSerializer,AnswerSerializer,TagSerializer
from django.shortcuts import render


class QCreate(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer


class QList(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

class QDetail(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer


class QUpdate(generics.RetrieveUpdateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer


class QDelete(generics.RetrieveDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer



class ACreate(generics.CreateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class AList(generics.ListAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer

class ADetail(generics.RetrieveAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class AUpdate(generics.RetrieveUpdateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class ADelete(generics.RetrieveDestroyAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class TCreate(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class TList(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class TDetail(generics.RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class TUpdate(generics.RetrieveUpdateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class TDelete(generics.RetrieveDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer