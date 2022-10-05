#!/bin/bash
set -e

mongo -u "artem" -p "0000"<<EOF
use admin 
db.createUser(
  {
    user: "artem",
    pwd: "0000",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)

use serv_2_db
db.createCollection("text")
db.text.insertOne({"text": "hello world"})
EOF