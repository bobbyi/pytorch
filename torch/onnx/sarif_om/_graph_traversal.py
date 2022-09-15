# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class GraphTraversal(object):
    """Represents a path through a graph."""

    description = attr.ib(default=None, metadata={"schema_property_name": "description"})
    edge_traversals = attr.ib(default=None, metadata={"schema_property_name": "edgeTraversals"})
    immutable_state = attr.ib(default=None, metadata={"schema_property_name": "immutableState"})
    initial_state = attr.ib(default=None, metadata={"schema_property_name": "initialState"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    result_graph_index = attr.ib(default=-1, metadata={"schema_property_name": "resultGraphIndex"})
    run_graph_index = attr.ib(default=-1, metadata={"schema_property_name": "runGraphIndex"})
