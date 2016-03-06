Readme.md


# vitual env
source myvenv/bin/activate

#Installation 

djangocms -f -p . ann

python manage.py runserver



# Dumpdata

##tout le site
python manage.py dumpdata -o data.json


##uniquement les oeuvres
python manage.py dumpdata galerie.oeuvre -o data_oeuvre.json



#charger les données
python manage.py loaddata /home/yogis/Projects/ann/data.json




# Déploiement serveur pythonanywhere
Voir la documentation DjangoGirls

# install et init du repo
git init
# config git
 git config --global user.name hugo.roussaffa
 git config --global user.email geodatup@gmail.com

# .gitignore



git add -A .
git commit -m "init"

# publier sur le nouveau repo

git remote add origin https://github.com/geodatup/ann.git
git push origin master


# sur pi
git clone https://github.com/geodatup/quorelcms.git

# créer un env virtuel
cd quorelcms
virtualenv --python=python3.4 myvenv
source myvenv/bin/activate

# installer django et les requierment (requirement.mb)
...

# deplacer les fichiers media
# load le dump
```
python manage.py loaddata data_final.json
```

#puis collecter les fichiers static
python manage.py collectstatic


# lancer la migration
Necéssite de créer un autre projet cms à coté puis de lancer 
python manage.py migrate 
dans le projet quorelcms
(sinon ça ne marche pas... la table n'existe pas dit il...)


# creer le super utilisateur
python manage.py createsuperuser



#Commande GIT 
###DEPUIS POSTE DEV
git add -A .
git commit -m "auto comment"
git push origin master



###clone Git (1er déployement)

git clone https://github.com/yougis/QuOrEL.git


virtualenv --python=python3.4 myvenv
source myvenv/bin/activate


pip install Django==1.9 whitenoise
pip install django-leaflet
pip install django-geojson
pip install django-import-export
pip install mysqlclient


# create database
mysql 
pwsd : mcot9a9.t

python manage.py collectstatic







###DEPUIS POSTE QUALIF - Pythonanywhere (myvenv)
cd /QuOrEl
git pull

python manage.py migrate

