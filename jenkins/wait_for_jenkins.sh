#!/bin/bash

#URL="http://jenkins:8080/login"
#TIMEOUT=120
#
#echo "Waiting for Jenkins to become ready at $URL..."
#
#for i in $(seq 1 $TIMEOUT); do
#  STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
#
#  if [[ "$STATUS" == "200" ]]; then
#    echo "Jenkins is READY!"
#    exit 0
#  fi
#
#  echo "[$i/$TIMEOUT] Jenkins not ready yet... status=$STATUS"
#  sleep 1
#done
#
#echo "ERROR: Jenkins did not start in time!"
#exit 1
set -e

echo "Waiting for Jenkins API token..."

TOKEN_FILE="/var/jenkins_home/api-token"

# ждём до 120 секунд
for i in {1..120}; do
  if [ -f "$TOKEN_FILE" ]; then
    break
  fi
  sleep 1
done

if [ ! -f "$TOKEN_FILE" ]; then
  echo "ERROR: Jenkins API token was not created"
  exit 1
fi

export JENKINS_TOKEN=$(cat "$TOKEN_FILE")
echo "Jenkins token loaded"

exec "$@"
