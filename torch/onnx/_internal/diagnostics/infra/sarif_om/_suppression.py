# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class Suppression(object):
    """A suppression that is relevant to a result."""

    kind = attr.ib(metadata={"schema_property_name": "kind"})
    guid = attr.ib(default=None, metadata={"schema_property_name": "guid"})
    justification = attr.ib(
        default=None, metadata={"schema_property_name": "justification"}
    )
    location = attr.ib(default=None, metadata={"schema_property_name": "location"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    state = attr.ib(default=None, metadata={"schema_property_name": "state"})


# flake8: noqa
