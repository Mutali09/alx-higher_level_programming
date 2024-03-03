#!/bin/bash
# This script takes a URL, sends a GET request using curl, and displays the body of the response if the status code is 200.

# Check if the user has provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided by the user
url=$1

# Send a GET request to the URL and store the response body
response=$(curl -s -w "%{http_code}" $url)

# Extract the status code from the response
status_code=$(tail -c 3 <<< "$response")
body=$(head -c -3 <<< "$response")

# Check if the status code is 200 (OK)
if [ $status_code -eq 200 ]; then
    # Display the body of the response
    echo "$body"
else
    echo "Error: HTTP status code $status_code"
fi
