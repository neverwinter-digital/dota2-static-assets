#!/bin/bash
cd /usr/local/crawler
echo "Cron job starts $1"
python $1_crawler.py # run the crawler
yes | cp -TR ../images/$1 /var/www/$1 # copy the images
