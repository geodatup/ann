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




