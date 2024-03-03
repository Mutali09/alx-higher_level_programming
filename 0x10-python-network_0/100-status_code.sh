#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response.

# Check if the user has provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided by the user
url=$1

# Send a HEAD request to the URL and store the response headers
response_headers=$(curl -s -o /dev/null -w "%{http_code}" $url)

# Display the status code
echo "$response_headers"
