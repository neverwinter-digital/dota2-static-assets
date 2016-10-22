# Give execution rights on the cron job
chmod 0644 /etc/cron.d/hello-cron

# Create the log file to be able to run tail
touch /var/log/cron.log

export STEAM_API_KEY=A72DE7D7BE9870C8DA671D67941CCAA7
export SAVE_PATH=../images
export VOLUMN_PATH=/var/www
export DB_URL=$POSTGRES_URL
export DB_NAME=$POSTGRES_DATABASE
export DB_PORT=$POSTGRES_PORT
export DB_USER=$POSTGRES_USERNAME
export DB_PASSWORD=$POSTGRES_PASSWORD

mkdir /usr/local/images/
mkdir /var/www
chmod +x /usr/local/crawler/run_crawler.sh
pip install --requirement /usr/local/crawler/requirement.txt
printenv | sed 's/^\(.*\)$/export \1/g' > /root/project_env.sh