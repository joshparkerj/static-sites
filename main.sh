#! /bin/bash
cp static/index.css static/styles.css
python3 src/main.py
cd public
pm2 start --name ssg python3 -- -m http.server 8888

