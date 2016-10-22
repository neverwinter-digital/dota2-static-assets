FROM kyma/docker-nginx
RUN apt-get update -y
RUN apt-get install -yqq cron libpq-dev python-dev python-pip libyaml-dev rsyslog vim

ENV STEAM_API_KEY=A72DE7D7BE9870C8DA671D67941CCAA7
ENV SAVE_PATH=../images
ENV VOLUMN_PATH=/var/www
ENV DB_URL=$POSTGRES_URL
ENV DB_NAME=$POSTGRES_DATABASE
ENV DB_PORT=$POSTGRES_PORT
ENV DB_USER=$POSTGRES_USERNAME
ENV DB_PASSWORD=$POSTGRES_PASSWORD

ADD setup.sh /root/setup.sh
# Set up cron
ADD crontab /etc/cron.d/hello-cron
# Copy the crawler to container
RUN mkdir /usr/local/crawler
COPY crawler /usr/local/crawler/

RUN /root/setup.sh

CMD rsyslogd && cron && nginx
