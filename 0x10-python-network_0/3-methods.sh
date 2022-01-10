#!/bin/bash
# URL and displays all HTTP methods the server
curl -sX "$1" | awk '/Allow/ { print $2 }'
