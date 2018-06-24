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
Necéssite de créer un autre projet cms et d'utiliser sa base project.db comme base sur laquelle lancer 
python manage.py migrate depuis dans le projet ann

```
Operations to perform:
  Synchronize unmigrated apps: treebeard, djangocms_admin_style, staticfiles, cmsplugin_filer_file, cmsplugin_filer_utils, cmsplugin_filer_video, sitemaps, import_export, gunicorn, cmsplugin_filer_teaser, sekizai, messages, cmsplugin_filer_folder, cmsplugin_filer_image
  Apply all migrations: easy_thumbnails, djangocms_googlemap, admin, contenttypes, djangocms_style, sites, sessions, djangocms_column, djangocms_link, cms, djangocms_text_ckeditor, djangocms_inherit, auth, menus, filer
Synchronizing apps without migrations:
  Creating tables...
    Creating table cmsplugin_filer_image_filerimage
    Creating table cmsplugin_filer_file_filerfile
    Creating table cmsplugin_filer_folder_filerfolder
    Creating table cmsplugin_filer_teaser_filerteaser
    Creating table cmsplugin_filer_video_filervideo
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states...Traceback (most recent call last):
  File "manage.py", line 10, in <module>
    execute_from_command_line(sys.argv)
  File "/var/www/django/ann/myvenv/lib/python3.5/site-packages/django/core/management/__init__.py", line 354, in execute_from_command_line
    utility.execute()
  File "/var/www/django/ann/myvenv/lib/python3.5/site-packages/django/core/management/__init__.py", line 346, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/var/www/django/ann/myvenv/lib/python3.5/site-packages/django/core/management/base.py", line 394, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/var/www/django/ann/myvenv/lib/python3.5/site-packages/django/core/management/base.py", line 445, in execute
    output = self.handle(*args, **options)
  File "/var/www/django/ann/myvenv/lib/python3.5/site-packages/django/core/management/commands/migrate.py", line 222, in handle
    executor.migrate(targets, plan, fake=fake, fake_initial=fake_initial)
  File "/var/www/django/ann/myvenv/lib/python3.5/site-packages/django/db/migrations/executor.py", line 100, in migrate
    state.apps  # Render all real_apps -- performance critical
  File "/var/www/django/ann/myvenv/lib/python3.5/site-packages/django/utils/functional.py", line 59, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/var/www/django/ann/myvenv/lib/python3.5/site-packages/django/db/migrations/state.py", line 166, in apps
    return StateApps(self.real_apps, self.models)
  File "/var/www/django/ann/myvenv/lib/python3.5/site-packages/django/db/migrations/state.py", line 232, in __init__
    self.render_multiple(list(models.values()) + self.real_models)
  File "/var/www/django/ann/myvenv/lib/python3.5/site-packages/django/db/migrations/state.py", line 270, in render_multiple
    "for more" % (new_unrendered_models, get_docs_version())
django.db.migrations.state.InvalidBasesError: Cannot resolve bases for [<ModelState: 'cmsplugin_filer_file.FilerFile'>, <ModelState: 'cmsplugin_filer_video.FilerVideo'>, <ModelState: 'cmsplugin_filer_teaser.FilerTeaser'>, <ModelState: 'cmsplugin_filer_folder.FilerFolder'>, <ModelState: 'cmsplugin_filer_image.FilerImage'>]
This can happen if you are inheriting models from an app with migrations (e.g. contrib.auth)
 in an app with no migrations; see https://docs.djangoproject.com/en/1.8/topics/migrations/#dependencies for more
```



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


