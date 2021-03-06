from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from django.core.validators import MinValueValidator



class Projet(models.Model):
    titre = models.CharField(max_length=100)
    content = models.TextField(verbose_name=('Contenu'))
    montant = models.PositiveSmallIntegerField(default=0)
    montantVoulu = models.PositiveSmallIntegerField(default=0, verbose_name=('Montant nécessaire pour démarrer le projet'))
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


class Contribution(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    contributeur = models.ForeignKey(User, on_delete=models.CASCADE)
    montantContribution = models.IntegerField(validators=[MinValueValidator(1)],verbose_name=('Montant de la contribution'))
    dateContribution = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ('Contribution de {} sur le projet {} (montant donné - {})'
            .format(self.contributeur.username, self.projet.titre, self.montantContribution))

    def get_absolute_url(self):
        return reverse("plateforme-view-projet-details", kwargs={"pk": self.projet.pk})
    
    