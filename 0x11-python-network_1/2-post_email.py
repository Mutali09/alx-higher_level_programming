#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Assuming the script takes URL and email as command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        # Send POST request using urllib
        with urllib.request.urlopen(url, data=data) as response:
            # Read and decode the response body
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.URLError as e:
        print("Error occurred:", e.reason)

