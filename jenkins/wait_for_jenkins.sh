#!/bin/bash

URL="http://jenkins:8080/login"
TIMEOUT=120

echo "Waiting for Jenkins to become ready at $URL..."

for i in $(seq 1 $TIMEOUT); do
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

  if [[ "$STATUS" == "200" ]]; then
    echo "Jenkins is READY!"
    exit 0
  fi

  echo "[$i/$TIMEOUT] Jenkins not ready yet... status=$STATUS"
  sleep 1
done

echo "ERROR: Jenkins did not start in time!"
exit 1
