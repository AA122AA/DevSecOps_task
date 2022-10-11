FROM docker.elastic.co/beats/metricbeat:7.16.1

# RUN curl -X POST "kibana:5601/api/index_patterns/index_pattern" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d '{"index_pattern": {"title": "metricbeat*", "timeFieldName": "@timestamp", "fields": "{}", "typeMeta": "{}", "fieldAttrs": "{}", "runtimeFieldMap": "{}"}}'
# CMD ["sleep", "20s", "&&", "curl", "-X", "POST", "kibana:5601/api/index_patterns/index_pattern", "-H 'kbn-xsrf: true'", "-H 'Content-Type: application/json'", "-d", "'{\"index_pattern\": {\"title\": \"metricbeat*\", \"timeFieldName\": \"@timestamp\", \"fields\": \"{}\", \"typeMeta\": \"{}\", \"fieldAttrs\": \"{}\", \"runtimeFieldMap\": \"{}\"}}'"]
COPY ./create_index.sh /config/create_index.sh
COPY ./dashboard.ndjson /config/dashboard.ndjson
WORKDIR /config
CMD ["./create_index.sh"]