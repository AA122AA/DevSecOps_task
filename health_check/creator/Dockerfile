FROM alpine
RUN apk --no-cache add curl
COPY ./create_index.sh /config/create_index.sh
COPY ./dashboard.ndjson /config/dashboard.ndjson
WORKDIR /config
CMD ["sh", "./create_index.sh"]
# RUN ./create_index.sh