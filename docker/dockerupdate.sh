#!/bin/bash
cd /home/tbsmarthome/smarthome
docker-compose down $1 $2 $3
docker-compose pull $1 $2 $3
docker-compose up -d $1 $2 $3