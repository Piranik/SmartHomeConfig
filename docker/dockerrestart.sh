#!/bin/bash
cd /home/tbsmarthome/smarthome
docker-compose stop $1
docker-compose start $1