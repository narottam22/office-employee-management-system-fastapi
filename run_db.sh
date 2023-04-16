#!/usr/bin/env bash

docker run -d \
  --name office_db \
  -p 7000:5432 \
  -e POSTGRES_DB=office_mgmt \
  -e POSTGRES_USER=admin_user \
  -e POSTGRES_PASSWORD=admin_password \
  postgres:13.4-alpine3.14 postgres
