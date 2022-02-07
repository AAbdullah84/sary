from django.db import models

class Tags(models.Model):
    tag = models.CharField(max_length=30)


class Questions(models.Model):
    question = models.CharField("Question", max_length=240, blank=False)
    created = models.DateField(auto_now_add=True)
    # tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.question



class Answers(models.Model):
    question =  models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField('Answer',max_length=120, blank=False)

    def __str__(self):
        return self.answer