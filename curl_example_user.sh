#! /bin/bash -ex

echo "Looking up stuff for $1..."

/usr/bin/curl -X POST \
-H "Authorization: bearer $GITHUB_TOKEN" \
-d '{ "query": "query { user(login: \"'$1'\") { login company }}"
}' https://api.github.com/graphql
