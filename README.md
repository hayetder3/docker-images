# docker-images
## Instructions de lancement
## Registre Docker Hub

Les images construites sont publiées et disponibles publiquement :
Dépôt : [hub.docker.com/repository/docker/hayetderdour/docker-images](https://hub.docker.com/repository/docker/hayetderdour/docker-images/general)

### Récupérer les images directement

docker pull hayetderdour/docker-images:nginx-v1
docker pull hayetderdour/docker-images:versioning-v1
docker pull hayetderdour/docker-images:versioning-v2
docker pull hayetderdour/docker-images:env-variables-1.0
docker pull hayetderdour/docker-images:python-app-1.0
###Cloner le projet
git clone [https://github.com/hayetder3/docker-images.git](https://github.com/hayetder3/docker-images.git)
cd docker-images
###Nginx Statique (Port 8080)
cd nginx
sudo docker build -t tp-nginx:v1 .
sudo docker run -d -p 8080:80 --name nginx-c tp-nginx:v1
curl http://localhost:8080
cd ..
####Versioning applicatif (Ports 8081 & 8082)
cd versioning

# Version 1
sudo docker build -t tp-versioning:v1 .
sudo docker run -d -p 8081:80 --name app-v1 tp-versioning:v1
curl http://localhost:8081

# Version 2 (après modification du fichier index.html)
sudo docker build -t tp-versioning:v2 .
sudo docker run -d -p 8082:80 --name app-v2 tp-versioning:v2
curl http://localhost:8082

cd ..
####Variables d'environnement
cd env-variables
sudo docker build -t tp-env:1.0 .

# Test par défaut
sudo docker run --rm tp-env:1.0

# Test avec surcharge runtime
sudo docker run --rm -e APP_MESSAGE="Mon message personnalise" tp-env:1.0

cd ..
####Application Python JSON (Port 5000)
cd python-app
sudo docker build -t tp-python-app:1.0 .
sudo docker run -d -p 5000:5000 --name python-c tp-python-app:1.0
curl http://localhost:5000
cd ..
