#! /bin/bash -e

/usr/bin/curl -X POST \
-H "Authorization: bearer $GITHUB_TOKEN" \
-d '{
  "query": "query { viewer { login company }}"
}' https://api.github.com/graphql
