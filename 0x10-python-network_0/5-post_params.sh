#!/bin/bash
#  sends a POST request to the passed URL
curl -sX POST -d "email=test@gmail.com&subjectI will always be here for PLD" "$1"
