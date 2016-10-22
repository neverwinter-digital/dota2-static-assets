FROM kyma/docker-nginx
RUN apt-get update -y
RUN apt-get install -yqq cron libpq-dev python-dev python-pip libyaml-dev rsyslog

ADD setup.sh /root/setup.sh
# Set up cron
ADD crontab /etc/cron.d/hello-cron
# Copy the crawler to container
RUN mkdir /usr/local/crawler
COPY crawler /usr/local/crawler/

RUN /root/setup.sh

CMD rsyslogd && cron && nginx
