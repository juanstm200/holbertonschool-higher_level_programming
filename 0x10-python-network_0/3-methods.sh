#!/bin/bash
# URL and displays all HTTP methods the server
curl -sI "$1" | awk '/Allow/' | sed -ne 's/^Allow: //p'
