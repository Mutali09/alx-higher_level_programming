#!/bin/bash

# Check if the user has provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided by the user
url=$1

# Send a GET request to the URL and store the response body
response=$(curl -s -o temp.txt -w "%{http_code}" $url)

# Extract the status code from the response
status_code=$(tail -n1 temp.txt)
body=""

# Check if the status code is 200 (OK)
if [ $status_code -eq 200 ]; then
    # Display the body of the response
    body=$(sed '$d' temp.txt)
    echo "$body"
else
    echo "Error: HTTP status code $status_code"
fi

# Clean up temporary file
rm -f temp.txt
