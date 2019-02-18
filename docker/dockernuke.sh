#!/bin/bash
cd /home/tbsmarthome/smarthome
docker-compose down
docker system prune --all --volumes
docker-compose up -d