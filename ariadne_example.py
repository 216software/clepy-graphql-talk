# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import os
import textwrap

import psycopg2
from ariadne import load_schema_from_path
from ariadne import ObjectType
from ariadne.wsgi import GraphQL
from ariadne import make_executable_schema

query = ObjectType("Query")

@query.field("demo")
def resolve_demo_query(_, info):

    return dict(
        current_timestamp="placeholder current_timestamp...",
        bogus_field_a="AAA",
        bogus_field_b="BBB")

@query.field("current_timestamp")
def resolve_current_timestamp(_, info):

        pgconn = info.context["pgconn"]
        cursor = pgconn.cursor()
        cursor.execute("select current_timestamp")
        return cursor.fetchone()[0]

@query.field("upcoming_shows")
def resolve_upcoming_shows(_, info):

def build_app():

    if "PGCONN" not in os.environ:
        raise Exception("Sorry, I need a connection string!")

    else:

        pgconn = psycopg2.connect(os.environ["PGCONN"])

        schema = make_executable_schema(
            load_schema_from_path("bogus_schema.graphql"),
            query)

        app = GraphQL(schema, debug=True,
            context_value=dict(pgconn=pgconn))

        return app

if __name__ == "__main__":

    print(textwrap.dedent("""Do this:

        gunicorn --reload "ariadne_example:build_app()"

    """))
