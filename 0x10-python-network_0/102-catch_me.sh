#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing "You got me!" in the body of the response.

# Send a PUT request to the URL and set the User-Agent header to "Holberton School"
curl -s -X PUT -H "User-Agent: Holberton School" -d "user_id=98" 0.0.0.0:5000/catch_me
