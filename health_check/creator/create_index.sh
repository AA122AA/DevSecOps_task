#!/bin/bash

sleep 20s
curl -X POST "kibana:5601/api/index_patterns/index_pattern" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d '{"index_pattern": {"title": "metricbeat*", "timeFieldName": "@timestamp", "fields": "{}", "typeMeta": "{}", "fieldAttrs": "{}", "runtimeFieldMap": "{}"}}'
curl -X POST "kibana:5601/api/saved_objects/_import?createNewCopies=true" -H "kbn-xsrf: true" --form file=@dashboard.ndjson -H 'kbn-xsrf: true'

