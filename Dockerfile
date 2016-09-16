FROM kyma/docker-nginx
RUN apt-get update -y
RUN apt-get install -yqq cron libpq-dev python-dev python-pip libyaml-dev rsyslog

# Set up cron
ADD crontab /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

ENV SAVE_PATH=../images
ENV VOLUMN_PATH=/var/www

# Copy the crawler to container
RUN mkdir /usr/local/crawler
COPY crawler /usr/local/crawler/
RUN mkdir /usr/local/images/
RUN mkdir /var/www
RUN chmod +x /usr/local/crawler/run_crawler.sh
RUN pip install --requirement /usr/local/crawler/requirement.txt
RUN printenv | sed 's/^\(.*\)$/export \1/g' > /root/project_env.sh

CMD rsyslogd && cron && nginx
