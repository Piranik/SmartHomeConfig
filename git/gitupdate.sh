#!/bin/bash

#cd /users/server/.homeassistant
# source /srv/homeassistant/homeassistant_venv/bin/activate
#hass --script check_config

#git rm -r --cached .
git add .
git status
echo -n "Enter the Description for the Change: [Minor Edit] "
read CHANGE_MSG
CHANGE_MSG=${CHANGE_MSG:-Minor Edit}
git commit -m "${CHANGE_MSG}"
git push origin master

exit