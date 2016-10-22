FROM kyma/docker-nginx
RUN apt-get update -y
RUN apt-get install -yqq cron libpq-dev python-dev python-pip libyaml-dev rsyslog

RUN ./setup.sh

CMD rsyslogd && cron && nginx
