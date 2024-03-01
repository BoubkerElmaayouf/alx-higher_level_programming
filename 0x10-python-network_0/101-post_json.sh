#!/bin/bash
# Curl a JSON file
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"