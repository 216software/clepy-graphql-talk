# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

from ariadne import load_schema_from_path
from ariadne import ObjectType

if __name__ == "__main__":

    schema = load_schema_from_path("bogus_schema.graphql")

