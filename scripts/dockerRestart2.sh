#!/bin/bash
while getopts n: arg 
do
  case "${arg}" in
    n) name="${OPTARG}";;
  esac
done

#Deleting Container and Name
sudo docker rm ${name}
sudo docker rmi ${name}

#changing directory to DOCKERFILE level
cd ..

#Build image
sudo docker build -t ${name} .

#Run container
docker run -p 3000:5000 --name ${name} -d ${name}