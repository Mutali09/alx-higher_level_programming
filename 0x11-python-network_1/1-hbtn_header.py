#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            request_id = response.headers.get('X-Request-Id')
            if request_id:
                print("Value of X-Request-Id:", request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print("Error occurred:", e.reason)
