from django.contrib import admin
from .models import *

# Register your models here.
class AdminAdministrateur(admin.ModelAdmin):
    list_display = ('id_admin', 'nom', 'poste', 'email', 'password')

class AdminLogement(admin.ModelAdmin):
    list_display = ('id_logement', 'type', 'numero', 'localisation', 'etat', 'qrcode')

class AdminEtudiant(admin.ModelAdmin):
    list_display = ('id_etudiant','nom','matricule','niveau','option','photo')

class AdminOccuper(admin.ModelAdmin):
    list_display = ('id_etudiant', 'id_logement')

admin.site.register(Administrateur, AdminAdministrateur)
admin.site.register(Etudiant, AdminEtudiant)
admin.site.register(Logement, AdminLogement)
admin.site.register(Occuper, AdminOccuper)
