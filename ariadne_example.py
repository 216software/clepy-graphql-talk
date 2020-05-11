# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import os
import textwrap

import psycopg2
from ariadne import load_schema_from_path
from ariadne import ObjectType
from ariadne.asgi import GraphQL

query = ObjectType("Query")

@query.field("upcoming_shows")
def resolve_upcoming_shows(obj, info):

    print(info.context)

def get_upcoming_shows(pgconn):

    cursor = pgconn.cursor()

    cursor.execute(textwrap.dedent("""
        select *
        from upcoming_shows
        """))

    return cursor

@query.field("current_timestamp")
def resolve_current_timestamp(_, info):

        cursor = pgconn.cursor()
        cursor.execute("select current_timestamp")
        return cursor.fetchone()[0]

def build_app():

    if "PGCONN" not in os.environ:
        raise Exception("Sorry, I need a connection string!")

    else:

        pgconn = psycopg2.connect(os.environ["PGCONN"])

        schema = load_schema_from_path("bogus_schema.graphql")

        app = GraphQL(schema, debug=True, context_value=dict(pgconn=pgconn))

        return app

if __name__ == "__main__":

    print(textwrap.dedent("""Do this:

        gunicorn --reload "ariadne_example:build_app()"

    """))
