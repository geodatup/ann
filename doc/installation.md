# virtual env
`source myvenv/bin/activate`
`workon myenv`

#Installation 

`djangocms -f -p . ann`


`export DJANGO_SETTINGS_MODULE=ann.settings.local`
`export DJANGO_SETTINGS_MODULE=ann.settings.production`

`python manage.py makemigrations galerie`
`python manage.py migrate`


`python manage.py runserver`



# Dumpdata
##Automatiquement aver crontab et Rsync

créer un fichier batch
~~~
#!/bin/sh

#########################################################
# Script to backup django website
# #########################################################
# directory which we save incremental changes to
BACKUPDIR=`date +%Y-%m-%d`


cd ~/production/ann

python manage.py dumpdata -o $BACKUPDIR/dumpdata.json

sudo cp -R media $BACKUPDIR/media

~~~

Sur le serveur/Nas configurer les taches de backup


##Manuellement 

###Tout le site

`python manage.py dumpdata -o dumpdata.json`
`sudo mv dumpdata.json /media/store/backup/`
`sudo cp -R /media/store/owncloud/data/yogis/files/projets/production/ann/media/ /media/store/backup/ann`

##uniquement les oeuvres
`python manage.py dumpdata galerie.oeuvre -o data_oeuvre.json`



#charger les données
`python manage.py loaddata /home/yogis/Projects/ann/data.json`




# Déploiement serveur pythonanywhere
Voir la documentation DjangoGirls

# install et init du repo
~~~
git init
# config git
 git config --global user.name hugo.roussaffa
 git config --global user.email geodatup@gmail.com

# .gitignore
~~~

~~~
git add -A .
git commit -m "init"
~~~

# publier sur le nouveau repo
~~~
git remote add origin https://github.com/geodatup/ann.git
git push origin master
~~~

# sur pi clone
~~~
git clone https://github.com/***.git
~~~

# sur client pull
~~~
git pull https://github.com/***.git master
~~~
# créer un env virtuel
~~~
cd ann
virtualenv --python=python3.4 myvenv
source myvenv/bin/activate
~~~

# installer django et les requierement (requirement.txt)

# lancer la migration d'un cms 
Necéssite de créer un autre projet cms à coté puis de lancer 
python manage.py migrate 
dans le projet ann
(sinon ça ne marche pas... la table n'existe pas dit il...)


# deplacer les fichiers media
# load le dump
```
python manage.py loaddata data_final.json
```

#puis collecter les fichiers static
~~~
python manage.py collectstatic
~~~



# creer le super utilisateur
~~~
python manage.py createsuperuser
~~~


