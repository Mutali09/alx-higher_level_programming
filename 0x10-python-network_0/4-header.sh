#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL with the specified header variable X-School-User-Id, and displays the body of the response.

# Check if the user has provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided by the user
url=$1

# Send a GET request to the URL with the specified header variable and store the response body
response=$(curl -s -H "X-School-User-Id: 98" $url)

# Display the body of the response
echo "$response"
