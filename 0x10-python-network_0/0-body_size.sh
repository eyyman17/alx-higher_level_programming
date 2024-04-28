#!/bin/bash
# Send a request to an URL and getting the body size
curl -sI "$1" | grep "Content-Length" | cut -c 17-
