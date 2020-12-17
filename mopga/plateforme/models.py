from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect


class Projet(models.Model):
    titre = models.CharField(max_length=100)
    content = models.TextField()
    dateCreation = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ('{}'.format(self.titre))

    def get_absolute_url(self):
        return reverse("plateforme-view-projet-details", kwargs={"pk": self.pk})


class Evaluation(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    evaluateur = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField()
    commentaire = models.TextField(max_length=500)
    dateEvaluation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ('Evaluation de {} sur le projet {} ({}/10 - {})'
            .format(self.evaluateur.username, self.projet.titre, self.note, self.commentaire))

    def get_absolute_url(self):
        return reverse("plateforme-view-projet-details", kwargs={"pk": self.projet.pk})
    
    