#!/usr/bin/python3
""" module doc """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    result = requests.get(url)
    print(result.headers.get("X-Request-Id"))
