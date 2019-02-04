List Docker Containers docker ps
Shell access (live container)	docker exec -it (container_name) /bin/bash
Realtime container logs	docker logs -f (container_name) 
Container version number	docker inspect -f '{{ index .Config.Labels "build_version" }}' (container_name) 
Image version number	docker inspect -f '{{ index .Config.Labels "build_version" }}' (container_name) 