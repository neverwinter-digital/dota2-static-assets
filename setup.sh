# Set up cron
ADD crontab /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

ENV STEAM_API_KEY=A72DE7D7BE9870C8DA671D67941CCAA7
ENV SAVE_PATH=../images
ENV VOLUMN_PATH=/var/www
ENV DB_URL=$POSTGRES_URL
ENV DB_NAME=$POSTGRES_DATABASE
ENV DB_PORT=$POSTGRES_PORT
ENV DB_USER=$POSTGRES_USERNAME
ENV DB_PASSWORD=$POSTGRES_PASSWORD

# Copy the crawler to container
RUN mkdir /usr/local/crawler
COPY crawler /usr/local/crawler/
RUN mkdir /usr/local/images/
RUN mkdir /var/www
RUN chmod +x /usr/local/crawler/run_crawler.sh
RUN pip install --requirement /usr/local/crawler/requirement.txt
RUN printenv | sed 's/^\(.*\)$/export \1/g' > /root/project_env.sh