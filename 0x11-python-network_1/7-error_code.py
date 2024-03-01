#!/usr/bin/python3
""" module doc """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    result = requests.get(url)
    if (result.status_code >= 400):
        print(f"Error code: {result.status_code}")
        exit()
    print(result.text)
