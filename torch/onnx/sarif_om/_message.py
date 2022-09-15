# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class Message(object):
    """Encapsulates a message intended to be read by the end user."""

    arguments = attr.ib(default=None, metadata={"schema_property_name": "arguments"})
    id = attr.ib(default=None, metadata={"schema_property_name": "id"})
    markdown = attr.ib(default=None, metadata={"schema_property_name": "markdown"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    text = attr.ib(default=None, metadata={"schema_property_name": "text"})
