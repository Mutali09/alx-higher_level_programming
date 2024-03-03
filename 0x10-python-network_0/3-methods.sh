#!/bin/bash
# This script takes a URL and displays all HTTP methods the server will accept.

# Check if the user has provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided by the user
url=$1

# Send an OPTIONS request to the URL and store the response headers
response_headers=$(curl -s -I -X OPTIONS $url)

# Extract the Allow header from the response headers
allowed_methods=$(grep -i '^Allow:' <<< "$response_headers" | sed 's/Allow: //i')

# Display the allowed HTTP methods
echo "$allowed_methods"
