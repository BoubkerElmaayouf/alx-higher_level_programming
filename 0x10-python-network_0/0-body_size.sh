#!/bin/bash
# curl body size
curl -sw '%{size_download}\n' -o /dev/null "$1"