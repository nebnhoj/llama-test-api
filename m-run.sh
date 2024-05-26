#!/bin/bash
echo "<==========================================================================>"
echo "Deploying core application..."

kill -9 $(lsof -ti:5601)
kill -9 $(lsof -ti:5602)
 
python index_server.py
