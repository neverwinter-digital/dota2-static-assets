# Give execution rights on the cron job
chmod 0644 /etc/cron.d/hello-cron

# Create the log file to be able to run tail
touch /var/log/cron.log

mkdir /usr/local/images/
mkdir /var/www
chmod +x /usr/local/crawler/run_crawler.sh
pip install --requirement /usr/local/crawler/requirement.txt
printenv | sed 's/^\(.*\)$/export \1/g' > /root/project_env.sh