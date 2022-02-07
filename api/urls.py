from django.urls import include, path
from .views import QCreate, QList, QDetail, QUpdate, QDelete, ACreate,AList,ADetail,AUpdate,TList,TCreate,TDelete,TDetail,TUpdate


urlpatterns = [
    path('', QList.as_view()),
    path('create/', QCreate.as_view(), name='create-question'),


    path('<int:pk>/', QDetail.as_view(), name='retrieve-question'),
    path('update/<int:pk>/', QUpdate.as_view(), name='update-question'),
    path('delete/<int:pk>/', QDelete.as_view(), name='delete-question'),

    path('answers/', AList.as_view()),
    path('createanswer/', ACreate.as_view(), name='create-answer'),

    path('answers/<int:pk>/', ADetail.as_view(), name='retrieve-answer'),
    path('answers/update/<int:pk>/', AUpdate.as_view(), name='update-answer'),
    path('answers/delete/<int:pk>/', QDelete.as_view(), name='delete-answer'),



    path('tags/', TList.as_view()),
    path('createtags/', TCreate.as_view(), name='create-tags'),

    path('tags/<int:pk>/', TDetail.as_view(), name='retrieve-tags'),
    path('tags/update/<int:pk>/', TUpdate.as_view(), name='update-tags'),
    path('tags/delete/<int:pk>/', TDelete.as_view(), name='delete-tags'),



]