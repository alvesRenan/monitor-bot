#!/bin/bash

# args: 
#   1-> password dockerhub
#   2-> bot key

docker build . -t renanalves/bot-monitor

docker login -u renanalves -p "${1}"
docker push renanalves/bot-monitor

sed -i 's@KEY_VALUE@'"${2}"'@' k8s-files/deployment.yaml
kubectl apply -f k8s-files
