#!/bin/sh

cd qapp && gunicorn -b 127.0.0.1:8080 qapp.wsgi
