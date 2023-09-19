#!/usr/bin/bash
openssl aes-256-cbc -pass pass:12345 -a -salt -d -in $1 -out $2