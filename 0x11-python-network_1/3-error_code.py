#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    # Assuming the script takes the URL as a command-line argument
    url = sys.argv[1]

    try:
        # Send request using urllib
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        # If HTTPError occurs, print the error code
        print("Error code:", e.code)

