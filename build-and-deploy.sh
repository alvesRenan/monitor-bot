#!/bin/bash

# args: 
#   1-> password dockerhub
#   2-> bot key

docker build . -t renanalves/bot-monitor

docker push -u renanalves -p $1 renanalves/test-app

sed -i 's@KEY_VALUE@'"${2}"'@' k8s-files/deployment.yaml
kubectl apply -f k8s-files