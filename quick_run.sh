source ~/myvenv/bin/activate
cd ~/Projects/ann/
export DJANGO_SETTINGS_MODULE=ann.settings.local
python manage.py runserver 0.0.0.0:8080
