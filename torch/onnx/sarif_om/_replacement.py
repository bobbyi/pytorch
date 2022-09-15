# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class Replacement(object):
    """The replacement of a single region of an artifact."""

    deleted_region = attr.ib(metadata={"schema_property_name": "deletedRegion"})
    inserted_content = attr.ib(default=None, metadata={"schema_property_name": "insertedContent"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
