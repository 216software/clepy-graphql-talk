# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import os
import pprint

import gql
import requests

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

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
            transport=sample_transport,
            fetch_schema_from_transport=True,
        )

        query = gql('''
            query getUserData($github_user: String!) {
                user(login: $github_user) {
                    login
                    company
                }
            }
        ''')

        query_vars = {"github_user":"bormesh"}

        x = client.execute(query, query_vars)

        print(type(x))
        pprint.pprint(x)
