#! /bin/bash
cp static/index.css static/styles.css
python3 src/main.py
cd public && python3 -m http.server 8888

