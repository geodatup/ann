#!/bin/sh

#########################################################
# Script to backup django website
# #########################################################
# directory which we save incremental changes to
BACKUPDIR=`date +%Y-%m-%d`


cd ~/production/ann

python manage.py dumpdata -o $BACKUPDIR/dumpdata.json

sudo cp -R media $BACKUPDIR/media


