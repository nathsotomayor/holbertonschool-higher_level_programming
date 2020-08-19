#!/bin/bash
# Displays only the status code of the response
curl -o /dev/null -s -w "%{http_code}" "$1"
