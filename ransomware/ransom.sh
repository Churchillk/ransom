#!/usr/bin/bash
openssl aes-256-cbc -pass pass:12345 -a -salt -in $1 -out $2
