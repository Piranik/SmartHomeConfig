List Docker Containers docker ps
Shell access (live container)	docker exec -it (container_name) /bin/bash
Realtime container logs	docker logs -f (container_name) 
Container version number	docker inspect -f '{{ index .Config.Labels "build_version" }}' (container_name) 
Image version number	docker inspect -f '{{ index .Config.Labels "build_version" }}' (container_name) 

## List Docker CLI commands
docker
docker container --help

## Display Docker version and info
docker --version
docker version
docker info

## Execute Docker image
docker run hello-world

## List Docker images
docker image ls

## List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq