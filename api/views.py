
from .models import Questions,Answers,Tags
from rest_framework import generics
from .serializers import QuestionSerializer,AnswerSerializer,TagSerializer
from django.shortcuts import render


class QCreate(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer


class QList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

class QDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer


class QUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer


class QDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer



class ACreate(generics.CreateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class AList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer

class ADetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class AUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class ADelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class TCreate(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class TList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class TDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class TUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class TDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Tags.objects.all()
    serializer_class = TagSerializer