# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class ReportingDescriptorRelationship(object):
    """Information about the relation of one reporting descriptor to another."""

    target = attr.ib(metadata={"schema_property_name": "target"})
    description = attr.ib(
        default=None, metadata={"schema_property_name": "description"}
    )
    kinds = attr.ib(
        default=attr.Factory(lambda: ["relevant"]),
        metadata={"schema_property_name": "kinds"},
    )
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})


# flake8: noqa
