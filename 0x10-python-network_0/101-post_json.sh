#!/bin/bash
# Sends a JSON POST request to a URL
curl -s "$1" -X POST -H "Content-Type: application/json" -d "@$2"
