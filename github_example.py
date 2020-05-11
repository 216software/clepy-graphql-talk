# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

# curl -H "Authorization: bearer $GITHUB_TOKEN" https://api.github.com/graphql

import os

import gql
import requests

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


# curl -H "Authorization: bearer $GITHUB_TOKEN" -X POST -d '
#  {
#         "query": "query { viewer { login company }}"
#          }
#          ' https://api.github.com/graphql
#          {"data":{"viewer":{"login":"mw44118","company":"216 Software,
#          LLC"}}}

if __name__ == "__main__":

    if "GITHUB_TOKEN" not in os.environ:
        raise Exception("Sorry, I need a GITHUB TOKEN!")

    else:

        sample_transport=RequestsHTTPTransport(
            url="https://api.github.com/graphql",
            use_json=True,
            headers={
                "Authorization": "bearer {GITHUB_TOKEN}".format(**os.environ),
                "Content-Type": "application/json",
            },
            verify=True
        )

        client = Client(
            retries=3,
            transport=sample_transport,
            fetch_schema_from_transport=True,
        )

        query = gql('''
            query {
                viewer {
                    login
                    company
                }
            }
        ''')

        x = client.execute(query)

        print(x)
