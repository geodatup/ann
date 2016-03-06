#Script reprise de donnée

python manage.py shell

from ann.apps.galerie.models import Rubrique, Oeuvre

oeuvre = Oeuvre(
   nom_oeuvre="Marquise",
   technique="",
   dimension="23 x 23cm",
   rubrique="",
   photo="",)

oeuvre.save()


rub= Rubrique(
nom_rubrique = Corrida
commentaire = "Oeuvre 1994, Exposition"
)