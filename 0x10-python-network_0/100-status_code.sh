#!/bin/bash
# status code of the response
curl --write-out "%{http_code}" --silent --output /dev/null "$1"
