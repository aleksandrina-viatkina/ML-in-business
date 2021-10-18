FROM python:3.9.2
WORKDIR /app
COPY . /app
EXPOSE 8183
RUN pip3 install -r requirements.txt
VOLUME /app/app/models
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
