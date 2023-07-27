from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw

# Create your models here.
class Administrateur(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=75)
    poste = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=75)

    class Meta:
        db_table = 'Administrateur'

    def __str__(self):
        return self.nom
    

class Etudiant(models.Model):
    id_etudiant = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=75)
    matricule = models.CharField(max_length=75)
    niveau = models.IntegerField()
    option = models.CharField(max_length=75)
    photo = models.ImageField(upload_to='photos',blank=True)

    class Meta:
        db_table = 'Etudiant'
    
    def __str__(self):
        return self.matricule

class Etat(models.Model):
    designation = models.CharField(max_length=15)

    def __str__(self):
        return self.designation 

class Logement(models.Model):
    id_logement = models.AutoField(primary_key=True)
    type = models.ForeignKey('Etat', models.CASCADE, db_column='designation')
    numero = models.IntegerField()
    localisation = models.CharField(max_length=75)
    etat = models.CharField(max_length=75)
    #qrcode = models.ImageField(upload_to='qr_code', null=True, blank=True)

    class Meta:
        db_table = 'Logement'

    def __int__(self):
        return self.numero

    # def save(self, *args, **kwargs):
    #     qr_image = qrcode.make(self.id_logement)
    #     canvas = Image.new('RGB', (qr_image.pixel_size, qr_image.pixel_size), 'white')
    #     draw = ImageDraw.Draw(canvas)
    #     canvas.paste(qr_image)
    #     file_name = f"qr_code-{self.id_logement}.png"
    #     buffer = BytesIO()
    #     canvas.save(buffer, 'PNG')
    #     self.qr_code.save(file_name, File(buffer), save=False)
    #     canvas.close()
    #     return super().save(*args, **kwargs)

class Occuper(models.Model):
    id_etudiant = models.ForeignKey('Etudiant', models.CASCADE, db_column='id_etudiant')
    id_logement = models.ForeignKey('Logement', models.CASCADE, db_column='id_logement')   

    class Meta:
        db_table = 'Occuper'
        unique_together = (('id_etudiant', 'id_logement'),)

    